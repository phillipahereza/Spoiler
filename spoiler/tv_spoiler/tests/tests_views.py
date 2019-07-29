from unittest.mock import patch, call

from django.test import TestCase
from django.urls import resolve

from spoiler.tv_spoiler.forms import VictimForm
from spoiler.tv_spoiler.models import Victim
from spoiler.tv_spoiler.utils import WELCOME_MESSAGE
from spoiler.tv_spoiler.views import HomeView


class TestHomePage(TestCase):
    def test_root_url_returns_OK_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_root_url_uses_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func.__name__, HomeView.as_view().__name__)

    def test_homepage_view_returns_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_homepage_returns_a_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], VictimForm)

    def test_submit_form_data_is_saved_on_post(self):
        TELEPHONE_NUMBER = "+256789997290"
        data = {
            "name": "Phillip",
            "telephone_number": TELEPHONE_NUMBER
        }
        response = self.client.post('/', data=data)
        self.assertEqual(Victim.objects.count(), 1)

    def test_on_form_save_user_redirected_to_root_page(self):
        TELEPHONE_NUMBER = "+256789997290"
        data = {
            "name": "Phillip",
            "telephone_number": TELEPHONE_NUMBER
        }
        response = self.client.post('/', data=data)
        self.assertRedirects(response, '/')

    @patch('spoiler.views.messages')
    def test_success_message_shown_on_victim_save_success(self, mock_messages):
        TELEPHONE_NUMBER = "+256789997290"
        data = {
            "name": "Phillip",
            "telephone_number": TELEPHONE_NUMBER
        }
        response = self.client.post('/', data=data)
        self.assertTrue(mock_messages.success.called)
        (request, message), kwargs = mock_messages.success.call_args
        self.assertEqual(request, response.wsgi_request)
        self.assertEqual(message,
                         'Spoilers will automatically be sent to your victim after the next episode airs')

    @patch('spoiler.views.messages')
    def test_success_message_shown_if_victim_already_exits(self, mock_messages):
        Victim.objects.create(telephone_number='+256789997290')
        data = {
            "name": "Phillip",
            "telephone_number": '+256789997290'
        }
        response = self.client.post('/', data=data)
        (request, message), kwargs = mock_messages.success.call_args
        self.assertEqual(request, response.wsgi_request)
        self.assertEqual(message,
                         'Spoilers will automatically be sent to your victim after the next episode airs')

    @patch("spoiler.views.send_welcome_message")
    def test_sms_sent_to_use_on_number_registered(self, mock_send_welcome_message):
        data = {
            "name": "Phillip",
            "telephone_number": '+256789997290'
        }
        _ = self.client.post('/', data=data)
        self.assertTrue(mock_send_welcome_message.called)
        (contact) = mock_send_welcome_message.call_args
        self.assertEqual(contact, call(["+256789997290"]))

    @patch("spoiler.utils.send_sms")
    def test_welcome_sms_has_correct_message(self, mock_send_sms):
        data = {
            "name": "Phillip",
            "telephone_number": '+256789997290'
        }
        _ = self.client.post('/', data=data)
        self.assertTrue(mock_send_sms.called)
        (message, contact), kwargs = mock_send_sms.call_args
        self.assertEqual(message, WELCOME_MESSAGE)


# class TestOptOutView(TestCase):
#     def test_slash_optout_returns_ok_response(self):
#         # /optout
#         response = self.client.get('/opt-out')
#         self.assertEqual(response.status_code, 200)








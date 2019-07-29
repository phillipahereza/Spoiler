from django.test import TestCase

from spoiler.tv_spoiler.forms import VictimForm
from spoiler.tv_spoiler.models import Victim


class TestVictimForm(TestCase):
    def test_form_renders_name_field(self):
        form = VictimForm()
        self.assertIn('name', form.as_p())

    def test_form_renders_telephone_number_field(self):
        form = VictimForm()
        self.assertIn('telephone_number', form.as_p())

    def test_form_has_placeholder_for_input_fields(self):
        form = VictimForm()
        self.assertIn('placeholder="Nickname"', form.as_p())
        self.assertIn('placeholder="+256782000000"', form.as_p())

    def test_form_handles_validation_for_empty_telephone_number_field(self):
        form = VictimForm(data={'name': 'Phillip'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['telephone_number'],
                         ['Telephone number field can not be empty'])

    def test_name_field_can_be_empty(self):
        form = VictimForm(data={'telephone_number': '+256782000000'})
        self.assertTrue(form.is_valid())

    def test_victim_saved_when_form_saved(self):
        form = VictimForm(
            data={'telephone_number': '+256782000000', 'name': 'Phillip'})
        form.save()
        self.assertEqual(Victim.objects.count(), 1)

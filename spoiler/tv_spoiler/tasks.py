import africastalking
from celery import shared_task
from django.conf import settings

from spoiler.tv_spoiler.models import Victim


@shared_task
def send_sms(spoiler_text: str):
    africastalking.initialize(settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY)
    sms = africastalking.SMS
    contacts = [victim['telephone_number'] for victim in Victim.objects.values()]

    try:
        sms.send(spoiler_text, contacts)
    except Exception as e:
        return e

@shared_task
def send_welcome_message(contact):
    africastalking.initialize(settings.AFRICASTALKING_USERNAME,
                              settings.AFRICASTALKING_API_KEY)
    sms = africastalking.SMS
    try:
        sms.send('Excited about Game of Thrones 😉😉 http://bit.ly/Ready4GoT', [contact])
    except Exception as e:
        pass


import africastalking
from django.conf import settings


def send_sms(spoiler_text: str, contacts: list):
    africastalking.initialize(settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY)
    sms = africastalking.SMS
    try:
        sms.send(spoiler_text, contacts)
    except Exception as e:
        return e

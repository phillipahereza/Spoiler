import africastalking
from django.conf import settings

africastalking.initialize(settings.AFRICASTALKING_USERNAME,
                          settings.AFRICASTALKING_API_KEY)

sms = africastalking.SMS

WELCOME_MESSAGE = "Excited about Game of Thrones 😉😉 http://bit.ly/Ready4GoT"


def send_sms(message: str, contacts: list):
    try:
        sms.send(message, contacts)
    except Exception:
        pass


def send_welcome_message(contacts: list):
    if isinstance(contacts, list):
        send_sms(WELCOME_MESSAGE, contacts)
    else:
        raise TypeError('contacts should be in a list')



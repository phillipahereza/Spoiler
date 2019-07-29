from celery import shared_task

from spoiler.tv_spoiler.utils import send_welcome_message


@shared_task
def send_welcome_message_task(contact: list):
    send_welcome_message(contact)
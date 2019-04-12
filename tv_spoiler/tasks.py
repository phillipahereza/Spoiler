import africastalking.SMS as SMS


def send_sms(spoiler_text: str, contacts: list[str]):
    try:
        SMS.send(spoiler_text, contacts)
    except Exception as e:
        return e

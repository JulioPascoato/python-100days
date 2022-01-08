from twilio.rest import Client

TWILIO_SID = "AC39e5059fc9ec307342322ceaa4d16a4f"
TWILIO_AUTH_TOKEN = "2b70eef32d90b7ee5a93c51337c58ed2"
TWILIO_VIRTUAL_NUMBER = "+13343397721"
TWILIO_VERIFIED_NUMBER = "+5511989453584"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
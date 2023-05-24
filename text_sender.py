from twilio.rest import Client
import os

# Twilio details retrieved from environmental variables

twilio_account_sid = os.environ["twilio_account_sid"]
twilio_auth_token = os.environ["twilio_auth_token"]
twilio_phone_num = os.environ["twilio_phone_num"]


class TextSender:

    def __init__(self):
        self.name = "name"
        self.phone = "phone"
        self.message = "message"

    def send_text(self, name, phone, message):
        client = Client(twilio_account_sid, twilio_auth_token)
        message_update = message.replace("[name]", f"{name}")
        destination_phone = phone
        send_message = client.messages \
            .create(
            body=message_update,
            from_=twilio_phone_num,
            to=destination_phone,
        )

        print(send_message.sid)

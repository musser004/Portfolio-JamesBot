import smtplib
import os


class EmailSender:

    # Contact information retrieved from environmental variables

    def __init__(self):
        self.name = "name"
        self.email = "email"
        self.my_gmail = os.environ["MY_GMAIL"]
        self.app_password = os.environ["GMAIL_APP_PASSWORD"]

    def send_email(self, name, email, message):

        # Message personalized with chosen user's name where applicable

        message_update = message.replace("[name]", f"{name}")
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.my_gmail, password=self.app_password)
            connection.sendmail(
                from_addr=self.my_gmail,
                to_addrs=email,
                msg=f"Subject: Hey there, it's a random message from JamesBot!\n\n{message_update}"
            )

# Application chooses a random person and message with randomizer, checks whether they've received a message
# previously with log_checker, then sends them a message via text_sender and/or email_sender

from email_sender import EmailSender
from text_sender import TextSender
from randomizer import Randomizer
from log_checker import Log_Checker
from datetime import datetime

# Checking whether the program should run, dependent on day of the week (Monday through Thursday only)

weekday = datetime.today().weekday()

# Manual weekday control (should remain commented out, if not in use)
# weekday = 1

# Randomizer chooses who will receive the message, and what message will be sent

randomizer = Randomizer()
name, phone_number, message_choice, choice, NUM_OF_AVAILABLE_MESSAGES, NUM_OF_USERS = randomizer.randomize()

if weekday < 4:

    # Log checker confirms that the message is new and not a repeat of a previously sent one (per each individual user)

    log_checker = Log_Checker()
    message_choice = log_checker.log_check(message_choice, NUM_OF_AVAILABLE_MESSAGES, name)

    # Chosen message is loaded

    with open(f"./message_templates/message_{message_choice}.txt", encoding="utf8") as file:
        message = file.read()

    # Format change for specific messages

    if message_choice == "01" or str(message_choice) == "10":
        name = name.upper()
        print(name)

    # email_sender and text_sender send message, dependent on variables

    text_sender = TextSender()
    email_sender = EmailSender()

    # Text messages for most users

    if choice < NUM_OF_USERS:
        text_sender.send_text(name=name, phone=phone_number, message=message)

    # Both text and email messages for one user

    else:
        text_sender.send_text(name=name, phone=phone_number, message=message)
        email_sender.send_email(name=name, email=randomizer.email_addy, message=message)

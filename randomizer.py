import os
from random import randint

# Constants (to be updated as more messages/users are added)

NUM_OF_AVAILABLE_MESSAGES = 42
NUM_OF_USERS = 6


class Randomizer:

    def __init__(self):
        self.names = ["Amelia", "Magan", "Patricia", "Keith", "Elite Nate", "James"]

        # Contact details retrieved from environmental variables

        self.phone_dict = {
            "Amelia": os.environ["AMELIA_NUMBER"],
            "Magan": os.environ["MAGAN_NUMBER"],
            "Patricia": os.environ["PATRICIA_NUMBER"],
            "Keith": os.environ["KEITH_NUMBER"],
            "Elite Nate": os.environ["NATE_NUMBER"],
            "James": os.environ["JAMES_NUMBER"]
        }
        self.email_addy = os.environ["JAMES_EMAIL"]

    def randomize(self):

        # randint chooses who will receive message today

        choice = randint(1, NUM_OF_USERS)

        # Manual choice control (should remain commented out, unless in use)
        # choice = 6

        print(f"Choice = {choice}")

        name = self.names[choice-1]
        phone_number = self.phone_dict[name]

        # randint chooses which message will be sent

        message_choice = randint(1, NUM_OF_AVAILABLE_MESSAGES)

        # Manual message control (should remain commented out, unless in use)
        # message_choice = 42

        # Message specific formatting

        if message_choice < 10:
            message_choice = f"0{message_choice}"

        # Outputs to main.py

        return name, phone_number, message_choice, choice, NUM_OF_AVAILABLE_MESSAGES, NUM_OF_USERS

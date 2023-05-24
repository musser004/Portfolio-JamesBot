from random import randint

class Log_Checker:
    def __init__(self):
        pass

    def log_check(self, message_choice, NUM_OF_AVAILABLE_MESSAGES, name):

        # Ultimately determines whether a message has already been sent, then picks a new one (if needed)
        # Log file is opened for the user chosen by randomizer

        try:
            file1 = open(f"./message_logs/{name}_log.txt", mode="r")

            # Log contents copied to variable, then log file is closed

            msg_log = file1.read()
            file1.close()

            # Printing total number of messages contained within log file

            num_of_used_messages = (len(msg_log) / 3)
            print(num_of_used_messages)

        # If log file does not exist, it is created here

        except FileNotFoundError:
            file1 = open(f"./message_logs/{name}_log.txt", mode="x")
            file1.close()
            num_of_used_messages = 0
            msg_log = ""

        message_choice = str(message_choice)
        msg_choice_is_new = False

        while msg_choice_is_new is False:
            if num_of_used_messages >= NUM_OF_AVAILABLE_MESSAGES:

                # clears the log file and writes the message_choice to the log if all messages have already been sent

                file1 = open(f"./message_logs/{name}_log.txt", mode="w")
                file1.write(f" {message_choice}")
                file1.close()
                msg_choice_is_new = True
            elif message_choice in msg_log:

                # if message_choice is in log, instead of re-rolling randomizer again, it just re-rolls the number here

                message_choice = randint(1, NUM_OF_AVAILABLE_MESSAGES)
                if message_choice < 10:
                    message_choice = f"0{message_choice}"
                else:
                    message_choice = str(message_choice)

                # since msg_choice_is_new remains False, loop will repeat until a message_choice that's not in the
                # log file is picked

            else:

                # since message_choice isn't in the log, this goes ahead and writes it to the log and exits loop

                file1 = open(f"./message_logs/{name}_log.txt", mode="a")
                file1.write(f" {message_choice}")
                file1.close()
                msg_choice_is_new = True

        # Chosen message has been logged and will be output in main.py

        print(f"Message choice = {message_choice}")
        return message_choice

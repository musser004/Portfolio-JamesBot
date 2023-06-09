# Project: JamesBot (Automation)

Description: Bot that does the following once a day via PythonAnywhere:
- Picks a random person from a contact list (contact details on environmental variables)
- Picks a random message from a list of templates. Messages include a compliment and a dumb joke about robots taking over the world
- Replaces any references to "name" within a template message to the chosen contact person's name
- Checks a log for each individual person to ensure that they've not received a given message before. If they have indeed already received the picked message, a new message is randomly  selected until it clears the log check successfully. If the log contains every available message (that person has received every available message), the log is fully cleared to restart the process
- Finally, the bot sends a message via text message (Twilio) and/or email (smtplib)

Python Libraries : Random, Datetime, Twilio, smtplib

NOTE: Application requires environmental variables (not included) in order to run properly

# How to use:

1.) Set up a Twilio account

2.) Update the Randomizer class self.phone_dict (line 17 of randomizer.py) to have the dictionary of names/phone numbers that you'd like to use

3.) Update the NUM_OF_USERS constant (line 7) in the same file to the new correct number

4.) Include all necessary environmental variables for individual user phone numbers/emails, "MY_GMAIL", "GMAIL_APP_PASSWORD", "twilio_account_sid", "twilio_auth_token", "twilio_phone_num"

5.) If you'd like to control which message is chosen, uncomment line 34 of randomizer.py and adjust the number

6.) If you'd like to manually change what day of the week it is according to the program (since it is set to only complete on Mondays through Thursdays), you can uncomment line 15 in main.py to any number from 0 to 3 (4/5/6 correlates to Friday/Saturday/Sunday, respectively)

7.) Program should run and will leave update log for each individual user

NOTE: If you'd like to automate this, it can be set up to run as a daily task on PythonAnywhere with a $5 start account

NOTE: You will also likely need to modify the if/else statements at the bottom of main.py if you'd like most users to also receive an email

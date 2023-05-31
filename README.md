# Project: JamesBot (Automation)

Description: Bot that does the following once a day via PythonAnywhere:
- Picks a random person from a contact list (contact details on environmental variables)
- Picks a random message from a list of templates. Messages include a compliment and a dumb joke about robots taking over the world
- Replaces any references to "name" within a template message to the chosen contact person's name
- Checks a log for each individual person to ensure that they've not received a given message before. If they have indeed already received the picked message, a new message is randomly  selected until it clears the log check successfully. If the log contains every available message (that person has received every available message), the log is fully cleared to restart the process
- Finally, the bot sends a message via text message (Twilio) and/or email (smtplib)

Python Libraries : Random, Datetime, Twilio, smtplib

NOTE: Application requires environmental variables (not included) in order to run properly

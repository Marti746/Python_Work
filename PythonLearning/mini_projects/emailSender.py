# Email Sender program
# 1.) go over to our gmail account and setup 2 factor authentication
# 2.) generate app password
# 3.) create a function to send the email
from email.message import EmailMessage
from secrets import EMAIL_PASSWORD
import ssl
import smtplib

# to improve I added a input to get the user input of what reciever they want to send
email_sender = "damartinco@gmail.com"
email_reciever = input("What is the recievers email address: ") # "mamojab953@vaband.com"

subject = input("What is the subject for the email: ") #"This is a Python Email Sender Test"
body = """This is a Python program that is sending an email through my account"""

# places all the information above into the proper places in the email template
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciever
em["subject"] = subject
em.set_content(body)

# try except block added to the project to allow for user input and to check if everything is okay that is being sent
# Basic level of error testing
try:
    context = ssl.create_default_context()

    # connect to the gmail SMPT server over the port 456 giving it the context from above
    # establishes a secure connection with Gmail's SMTP server over SSL/TLS on port 465, using the SSL context we created earlier, 
    # and assigns the SMTP client session object to the variable 'smtp' for further interaction.
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, EMAIL_PASSWORD)
        smtp.sendmail(email_sender, email_reciever, em.as_string())
        print("Email sent successfully!")

except smtplib.SMTPAuthenticationError:
    print("Authentication failed. Please check your email address and password.")

except smtplib.SMTPException as e:
    print("An error occurred while sending the email:", e)
# 1. Write Python Program that checks application.
# 2. Send Email, When website is down.
# 3. Automate fixing that problem: by restart docker container or server.

import requests
import smtplib
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

# print(response.text)  # This will provide the HTML code of application
# print(response.status_code)  # This will provide the status code like 200, 504...

'''
Note - 
If you have enable 2 step verification in your gmail account then you need
to generate "App Passwords" using link 'https:/myaccount.google.com/u/1/apppasswords'
use that code in smtp.login(). by providing that code inplace of password

If you have disable 2 step verification in your gmail account then you need
to enable "Less secure app" using link 'https:/myaccount.google.com/lesssecureapps'
then you can provide email-password to smtp.login() 
'''


def send_email(email_msg):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Subject: SITE DOWN\n{email_msg}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)  # we required sender email, recipient
        # email and message


try:
    response = requests.get('http://Python-App-370525590.ap-south-1.elb.amazonaws.com')  # Provide URL
    if response.status_code == 200:
        print("Application is running successfully")
    else:
        print("Application Down, Fix It")
        # Send Email to me
        msg = f"Application returned: {response.status_code}. Please configure to FIX the issue! Restart the App."
        send_email(msg)

except Exception as ex:
    print(f'Connection error happened: {ex}')
    msg = "Application isn't accessible at all."
    send_email(msg)

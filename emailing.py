import smtplib
import keyring
import imghdr
from email.message import EmailMessage
import os
import glob
SENDER = keyring.get_password("Gmail", "jadon")
PASSWORD = keyring.get_password("GmailPass", "jadon")
RECEIVER = SENDER

def clean_folder():
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    clean_folder()


if __name__ == "__main__":
    send_email(image_path="images/19.png")
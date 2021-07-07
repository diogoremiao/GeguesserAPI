import PySimpleGUI as sg
from MailApi.Mail import Mail
import webbrowser
import pyperclip

def create_mail():

    # Create Temp Mail Obj
    login = "temp_mail"
    mail_obj = Mail(login)

    # Get all domains
    domains = Mail.get_domains()

    # Chose one
    mail_obj.domain = domains.json()[0]

    # Get email address and copy to clipboard
    mail_obj.mail = mail_obj.get_mail_address()
    pyperclip.copy(mail_obj.mail)
    print("Mail copied to clipboard")

    # Open GeoGuesser create account link
    link = "https://www.geoguessr.com/signup"
    webbrowser.open(link, new=2)

    return mail_obj


def check_mail(mail_obj):

    # Check mailbox
    mail_elements = Mail.check_mail(mail_obj.get_mail_url())

    # Create password with 10 chars
    mail_obj.password = Mail.create_password(10)

    # Copy password to clipboard
    pyperclip.copy(mail_obj.password)
    print("Password copied to clipboard")

    # Get link to set password and open on browser (new tab)
    link = Mail.check_guesser_link(mail_elements)
    webbrowser.open(link, new=2)


layout = [[sg.Text("Press to create account")], [sg.Button("Create")], [sg.Button("Check Mail")]]

# Create the window
window = sg.Window("GeoGuesser Account Creator", layout, margins=(100, 50))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Create":
        mail_obj = create_mail()

    if event == "Check Mail":
        check_mail(mail_obj)
        break



window.close()

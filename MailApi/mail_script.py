from Mail import Mail
import webbrowser
import pyperclip


def main():

    # Create Temp Mail Obj
    login = "temp_mail"
    mail_obj = Mail(login)

    # Create password with 10 chars
    mail_obj.password = Mail.create_password(10)

    # Get all domains
    domains = Mail.get_domains()

    # Chose one
    mail_obj.domain = domains.json()[0]

    # Get email address and copy to clipboard
    mail_obj.mail = mail_obj.get_mail_address()
    pyperclip.copy(mail_obj.mail)
    print("Mail copied to clipboard")

    input("Waiting for mail to be sent...")

    # Check mailbox
    mail_elements = Mail.check_mail(mail_obj.get_mail_url())

    # Copy password to clipboard
    pyperclip.copy(mail_obj.password)
    print("Password copied to clipboard")

    # Get link to set password and open on browser (new tab)
    link = Mail.check_guesser_link(mail_elements)
    webbrowser.open(link, new=2)


if __name__ == '__main__':
    main()
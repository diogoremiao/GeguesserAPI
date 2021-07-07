import requests
import hashlib
import random
from bs4 import BeautifulSoup
import string

# Headers for authentication
headers = {
    'x-rapidapi-key': "ae3c2e4479msh02171dd206fbea7p189a43jsn70be968f5293",
    'x-rapidapi-host': "privatix-temp-mail-v1.p.rapidapi.com"
}


class Mail:

    # The init method/constructor
    def __init__(self, login):

        self.login = login
        self.password = None
        self.domain = None
        self.mail = None

    # Return list of available domains
    @staticmethod
    def get_domains():

        # URL for domain request
        url_domain = "https://privatix-temp-mail-v1.p.rapidapi.com/request/domains/"

        # Request containing vector with domains
        request = requests.get(url_domain, headers=headers)

        return request

    # Return complete mail address
    def get_mail_address(self):

        # Generate random mail
        mail = self.login + str(random.randint(1, 100000)) + self.domain

        return mail

    # Return URL to check mailbox
    def get_mail_url(self):

        # URL to check mailbox
        url_get = "https://privatix-temp-mail-v1.p.rapidapi.com/request/mail/id/"

        return url_get + hashlib.md5(self.mail.encode()).hexdigest() + "/"

    # Check mailbox
    @staticmethod
    def check_mail(url_get):

        # Request for mails
        response = requests.get(url_get, headers=headers)

        # Parse to HTML
        soup = BeautifulSoup(response.content, "html.parser")

        return soup

    # Check for set-password link
    @staticmethod
    def check_guesser_link(soup):

        # Password link template
        post_link = "https://www.geoguessr.com/profile/set-password/"

        # Search for entry
        link_element = soup.find(string=lambda text: "https://www.geoguessr.com/profile/set-password" in text.lower())

        # Build the string
        link = ""
        for i in range(1, len(link_element)):
            if link_element[i] == 'r' and link_element[i + 1] == 'd' and link_element[i + 2] == '/':
                for j in range(i + 3, 1000):
                    aux = link_element[j]
                    if aux != ']':
                        link += aux
                    else:
                        break

        return post_link + link

    # Generate Password
    @staticmethod
    def create_password(count):

        # Poll of chars
        char_poll = string.ascii_letters + string.digits + string.punctuation

        # Randomise
        password = "".join(random.sample(char_poll, count))

        return password



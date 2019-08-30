from bs4 import BeautifulSoup

def get_ticket_dict(html):
    ticket_dict = {}
    soup = BeautifulSoup(html,"html.parser")
    for tag in soup.find(name='error').children:
        ticket_dict[tag.name] = tag.text
    return ticket_dict
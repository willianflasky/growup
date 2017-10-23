html = """<error><ret>0</ret><message></message><skey>@crypt_2ccf8ab9_5b013c91e2de6ba5cac4b73f2bf8e258</skey><wxsid>N6zBt+tjkJfPJ1Vx</wxsid><wxuin>981579400</wxuin><pass_ticket>%2FEsidH%2BwbgFjSxKQADem8jIUxrUG%2B8lKT57jinMmRWoFPm2cD32HGjiXdXs4vqum</pass_ticket><isgrayscale>1</isgrayscale></error>"""

ticket_dict = {}
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,"html.parser")
for tag in soup.find(name='error').children:
    ticket_dict[tag.name] = tag.text
print(ticket_dict)


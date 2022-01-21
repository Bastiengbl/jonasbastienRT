#le code suivant récupère la page html linkedin de kevin marah dans le code python:
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.linkedin.com/in/k%C3%A9vin-marah-910629127/"
page = requests.get(URL)
#On crée ici un objet BeautifulSoup en passant deux arguments:(page.content et html5lib)
soup = BeautifulSoup(page.content, 'html5lib') #si cette ligne rencontre une erreur, installez 'pip install html5lib' ou 'install html5'
print(soup.prettify())
quotes=[] #liste pour récupérer les quotes
#on indique l'endroit ou scrapper:
table = soup.find('div', attrs = {'id':'profile-content'})
for row in table.findAll('div',
                    attrs = {'class':'text-heading-xlarge inline t-24 v-align-middle break-words'})
#on récupère toutes les informations que l'on veut dans les quotes
quote['nom'] = row.h1.text
    quote['travail'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)
   

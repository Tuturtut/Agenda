import requests
from bs4 import BeautifulSoup


loginUrl = 'https://fr.wikipedia.org/wiki/Liste_des_jeux_vid%C3%A9o_les_plus_vendus'


res = requests.get(loginUrl)


if res.ok:

    soup = BeautifulSoup(res.text, 'html.parser')

    with requests.Session() as s:
        r = s.get(loginUrl)
        soup = BeautifulSoup(r.text, 'html.parser')
        res = soup.find('table', {'class': 'wikitable sortable'})
        print(res.text)

else:
    print("Error")

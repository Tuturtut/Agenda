import requests
from bs4 import BeautifulSoup


loginUrl = 'https://auth.univ-lorraine.fr/login?service=https:%2F%2Fent.univ-lorraine.fr%2FLogin%3FrefUrl%3D%2F'
logedUrl = 'https://ent.univ-lorraine.fr/#Tous'

res = requests.get(loginUrl)

payload = {
    'username': 'simonin94u',
    'password': 'Tutursim88*'
}


if res.ok:

    soup = BeautifulSoup(res.text, 'html.parser')

    with requests.Session() as s:
        s.post(loginUrl, data=payload)

        r = s.get(logedUrl)

        print(r.text)

        soup = BeautifulSoup(r.text, 'html.parser')

        res = soup.find('a')

else:
    print("Error")

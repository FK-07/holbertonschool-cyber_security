import requests
from bs4 import BeautifulSoup

url = "http://web0x01.hbtn/a3/sql_injection/"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

for form in soup.find_all('form'):
    print("Form action:", form.get('action'))
    print("Form method:", form.get('method'))
    for inp in form.find_all(['input', 'button']):
        print(f" Input name: {inp.get('name')}, type: {inp.get('type')}")

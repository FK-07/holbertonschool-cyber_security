import requests
from bs4 import BeautifulSoup

url = "http://web0x01.hbtn/a3/sql_injection/"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

print("--- Linklər (A teqləri) ---")
for a in soup.find_all('a', href=True):
    print(a['href'])

print("--- Formalar ---")
for f in soup.find_all('form'):
    print("Action:", f.get('action'), "Method:", f.get('method'))

import requests

url = "http://web0x01.hbtn/a3/sql_injection/"
# Səhifənin cavabını və yönləndirmələri yoxlayaq
res = requests.get(url)
print("Status:", res.status_code)
print("Headers:", res.headers.get('Content-Type'))

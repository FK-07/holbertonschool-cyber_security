import requests

# Yüklənmiş PHP faylının tam ünvanı
url = "http://test-s3.web0x05.hbtn/static/upload/exploit2.php"

response = requests.get(url)
print("Status Code:", response.status_code)
print("Cavab (Flag):", response.text)

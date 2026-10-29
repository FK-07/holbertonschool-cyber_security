import concurrent.futures
import urllib.request

url_template = "http://10.42.113.77/{}/hbtn-{}"

with open("list_fuzz") as f:
    words = [line.strip() for line in f if line.strip()]

def check(w1, w2):
    url = url_template.format(w1, w2)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=3) as response:
            code = response.getcode()
            if code != 404:
                print(f"[+] TAPILDI!: {url} -> Status: {code}")
    except urllib.error.HTTPError as e:
        if e.code != 404:
            print(f"[+] TAPILDI!: {url} -> Status: {e.code}")
    except Exception:
        pass

print("[*] Fuzzing başladı...")
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    for w1 in words:
        for w2 in words:
            executor.submit(check, w1, w2)
print("[*] Bitdi.")

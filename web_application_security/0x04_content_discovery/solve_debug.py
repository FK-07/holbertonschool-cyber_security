import concurrent.futures
import urllib.request
import urllib.error

url_template = "http://web0x04.hbtn/{}/hbtn-{}"

with open("list_fuzz") as f:
    words = [line.strip() for line in f if line.strip()]

print(f"[*] Ümumi söz sayı: {len(words)}, Yoxlanılacaq kombinasiya: {len(words)**2}")

def check(w1, w2):
    url = url_template.format(w1, w2)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Host": "web0x04.hbtn"})
        with urllib.request.urlopen(req, timeout=5) as response:
            code = response.getcode()
            print(f"[İnfo] {url} -> Status: {code}")
            if code != 404:
                print(f"[+] TAPILDI!: {url} -> Status: {code}")
    except urllib.error.HTTPError as e:
        print(f"[İnfo] {url} -> HTTP Error: {e.code}")
        if e.code != 404:
            print(f"[+] TAPILDI!: {url} -> Status: {e.code}")
    except Exception as e:
        # Bağlantı xətalarını görmək üçün buranı açıq saxlayırıq
        # print(f"[Xəta] {url} -> {e}")
        pass

print("[*] Fuzzing başladı...")
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    for w1 in words:
        for w2 in words:
            executor.submit(check, w1, w2)
print("[*] Bütün sorğular göndərildi, gözlənilir...")

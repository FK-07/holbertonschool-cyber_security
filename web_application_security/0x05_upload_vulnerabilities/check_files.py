import requests

base_url = "http://test-s3.web0x05.hbtn"

# Ehtimal olunan API siyahı və fayl endpoint-ləri
api_endpoints = [
    "/api/files",
    "/api/list",
    "/api/task2/files",
    "/api/task1/",
    "/files",
    "/list"
]

for endpoint in api_endpoints:
    url = base_url + endpoint
    try:
        res = requests.get(url)
        print(f"Endpoint: {endpoint} | Status: {res.status_code}")
        if res.status_code == 200 and "html" not in res.text.lower():
            print(f"Məzmun: {res.text}")
    except Exception as e:
        print(f"Xəta: {e}")

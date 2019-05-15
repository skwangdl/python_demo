import requests

def demo_requests():
    url = "http://xportal-core-service.earth.xpaas.lenovo.com/deploy/resource-bundle"
    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"file\"; filename=\"C:\\Users\\issuser\\Desktop\\AutotestReport.zip\"\r\nContent-Type: application/zip\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'Authorization': "Bearer 5ebf2d74-71c1-49f2-b9fd-13a7bf7252eb",
        'cache-control': "no-cache",
        'Postman-Token': "c8a7cbe2-b9d4-4a2d-b09d-c1bd3e1efb24"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

if __name__ == '__main__':
    demo_requests()
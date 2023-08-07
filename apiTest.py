import requests

url = 'http://127.0.0.1:8000/uploadfile'
file = {'file': open('ReadMe.pdf', 'rb')}
resp = requests.post(url=url, files=file) 
print(resp.json())
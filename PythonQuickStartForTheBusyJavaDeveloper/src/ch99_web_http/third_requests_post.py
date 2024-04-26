import requests


# POST
payload = {'username':'Olivia','password':'123'}
r = requests.post('https://httpbin.org/post', data = payload)
print(r.text)
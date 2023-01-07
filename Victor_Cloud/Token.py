import json
import requests
# input
print("Victor smart kill authorization token request")
print("Enter username")
user = input()
print("Enter password")
pwd = input()

URL = "https://www.victorsmartkill.com/api-token-auth/"

headers = {
"accept": "application/json",
"Content-Type": "application/json"
}

params = {
"username": user,
"password": pwd
}

resp = requests.post(URL, headers = headers ,data=json.dumps(params))
tk = json.loads(resp.text)['token']

if resp.status_code != 200:
    print('error: ' + str(resp.status_code))
else:
    print('Token ' + str(tk))
    print('Success')
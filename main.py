import requests

def cmd_api_client(username):
    r = requests.get('http://127.0.1.1:5000/api/post/{}'.format(username))
    print(r.text)
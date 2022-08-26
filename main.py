import requests

client_id = 'b-62hjVEwKOQ8KL6_l0GCQ'
secret_token = 'VrI1N42e-TLtt7HWoLioxAYm1oOtSw'
auth = requests.auth.HTTPBasicAuth(client_id, secret_token)


data = {'grant_type': 'password',
        'username': 'TDZ6',
        'password': 'P6NRTARHcqqAf6@k'}

headers = {'User-Agent': 'CoqueBot/0.0.1'}

res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

TOKEN = res.json()['access_token']


headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

res = requests.get("https://oauth.reddit.com/r/AmItheAsshole/hot",
                   headers=headers)

for post in res.json()['data']['children']:
    print(post['data']['title'])

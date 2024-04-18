# %%
import os
import json
import datetime as dt
import requests


REPO = 'ghactions'
OWNER = 'ahnm1'
TOKEN = os.environ.get('GH_TOKEN')

now = str(dt.datetime.now())

url = f'https://api.github.com/repos/{OWNER}/{REPO}/dispatches'

data = json.dumps({
    "event_type": "test_result",
    "client_payload": {
        "passed": False,
        "message": f"Triggered by Python locally at: {now}"
    }
})

headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {TOKEN}',
    'X-GitHub-Api-Version': '2022-11-28',
}

r = requests.post(
    url=url,
    data=data,
    headers=headers
)

r.headers

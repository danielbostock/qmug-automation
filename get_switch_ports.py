import requests, json

url = "https://api.meraki.com/api/v0/devices/Q2HP-Q9S8-BVHB/switchPortStatuses"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

response = requests.request('GET', url, headers=headers, data = payload).json()

print(json.dumps(response, indent=2, sort_keys=True))

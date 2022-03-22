import requests
import json

# URL and DeviceName from NSO environment 
url_base = 'https://xx.xx.xx.xx:443'
device_name= 'core-rtr01'

# config headers + auth
headers = {
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic xxxxxxxxxxxxxx'
}

# Get device config from NSO
payload={}
response = requests.request("GET", f'{url_base}/restconf/data/tailf-ncs:devices/device={device_name}', headers=headers, data=payload, verify=False)

# Parse out device config from response body
json=json.loads(response.text)
device_config = json['tailf-ncs:device']
# Print device config
print("Device Config:")
print(f"Name: {device_config[0]['name']}")
print(f"IP: {device_config[0]['address']}")
print(f"Running Config: {device_config[0]['config']}")
print(" ")





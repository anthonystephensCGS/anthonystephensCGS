import requests
import json

url = "https://api.meraki.com/api/v1/organizations/xxxxxxxxxxxxxxxx/networks"

headers = {
    'accept': "*/*",
    'x-cisco-meraki-api-key': "xxxxxxxxxxxxxxxxxxxxxx",
    'cache-control': "no-cache",
    'postman-token': "5203d66a-d14e-dd1b-ecf4-c6c7507918d5"
    }

org_networks = requests.request("GET", url, headers=headers, verify=False)


with open(org_networks, "r") as json_file:
    networks = json.load(json_file)

for network in networks:
    for key, value in network.items():
        if key == "name":
            print('{}: {}'.format(key, value))

#print(org_networks.text)













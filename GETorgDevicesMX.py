import requests

url = "https://api.meraki.com/api/v1/organizations/xxxxxxxxxxxxxxxx/devices"

payload={}
headers = {
  'X-Cisco-Meraki-API-Key': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

#for devices in response.content:
    #if "model" == "MX65":


#print(response.content)
content=response.content
data=open("StoreMX.json","wb")
data.write(content)
data.close()

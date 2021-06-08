import requests

url = "https://api.meraki.com/api/v1/organizations/646829496481088052/devices"

payload={}
headers = {
  'X-Cisco-Meraki-API-Key': '2db0c8ddbfcde0ab2602c03ee56f6de0cac34899'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

#for devices in response.content:
    #if "model" == "MX65":


#print(response.content)
content=response.content
data=open("StoreMX.json","wb")
data.write(content)
data.close()
import requests

YOUR_IP = "255.255.255.255"

SiteUrlIp = "https://api.ipify.org/?format=json"

response = requests.get(SiteUrlIp)

#check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(data["ip"])
    YOUR_IP = str(data["ip"])
    SiteUrlGeo = "https://ipinfo.io/"+YOUR_IP+"/geo"
    response = requests.get(SiteUrlGeo)

    #check if the request was successful
    if response.status_code == 200:
        data = response.json()
        print(data)

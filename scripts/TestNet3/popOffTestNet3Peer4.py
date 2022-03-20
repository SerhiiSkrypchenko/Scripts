import requests

# Testnet 3
url1 = "http://51.15.250.32/apl"
url2 = "http://51.15.253.171/apl"
url3 = "http://51.15.210.116/apl"
url4 = "http://51.15.242.197/apl"
url5 = "http://51.15.218.241/apl"

querystring = {"requestType": "popOff", "adminPassword": "1", "height": "1"}

response = requests.request("POST", url4, params=querystring)
print(response.text)
print("----------------------------------------------------------------------")

#response = requests.request("POST", url2, params=querystring)
#print(response.text)
#print("----------------------------------------------------------------------")

#response = requests.request("POST", url3, params=querystring)
#print(response.text)
#print("----------------------------------------------------------------------")

#response = requests.request("POST", url4, params=querystring)
#print(response.text)
#print("----------------------------------------------------------------------")

#response = requests.request("POST", url5, params=querystring)
#print(response.text)
#print("----------------------------------------------------------------------")

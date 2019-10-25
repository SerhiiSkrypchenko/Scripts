import requests
import testNet3

querystring = {"requestType": "popOff", "adminPassword": "1", "height": "9900"}

response = requests.request("POST", testNet3.url1, params=querystring)
print(response.text)
print("----------------------------------------------------------------------")

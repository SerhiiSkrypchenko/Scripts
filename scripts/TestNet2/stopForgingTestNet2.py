import requests
import random
from tkinter import *

from tkinter import messagebox

# Test Net 3
url31 = "http://51.15.250.32/apl"
url32 = "http://51.15.253.171/apl"
url33 = "http://51.15.210.116/apl"
url34 = "http://51.15.242.197/apl"
url35 = "http://51.15.218.241/apl"
urls3 = random.choice([url31, url32, url33, url34, url35])
# Test Net 2
localhost = "http://localhost:7876/apl"
url21 = "http://51.15.247.49/apl"
url22 = "http://51.15.209.252/apl"
url23 = "http://51.15.228.90/apl"
url24 = "http://51.15.228.126/apl"
url25 = "http://51.15.228.171/apl"
url26 = "http://51.15.46.25/apl"
url27 = "http://51.15.72.23/apl"
url28 = "http://51.15.100.44/apl"
url29 = "http://51.15.233.93/apl"
urls2 = random.choice([localhost, url21, url22, url23, url24, url25, url26, url27, url28, url29])


# urls2 = random.choice([url21, localhost])

#querystring = {"requestType": "stopForging", "adminPassword": "1"}
#response = requests.request("POST", localhost, params=querystring)
#print(response.text)
#print("----------------------------------------------------------------------")

querystring = {"requestType": "stopForging", "adminPassword": "1"}
response = requests.request("POST", url21, params=querystring)
print(response.text)
print("----------------------------------------------------------------------")

querystring = {"requestType": "stopForging", "adminPassword": "1"}
response = requests.request("POST", url22, params=querystring)
print(response.text)
print("----------------------------------------------------------------------")

querystring = {"requestType": "stopForging", "adminPassword": "1"}
response = requests.request("POST", url23, params=querystring)
print(response.text)
print("----------------------------------------------------------------------")

querystring = {"requestType": "stopForging", "adminPassword": "1"}
response = requests.request("POST", url24, params=querystring)
print(response.text)
print("----------------------------------------------------------------------")

querystring = {"requestType": "stopForging", "adminPassword": "1"}
response = requests.request("POST", url25, params=querystring)
print(response.text)
print("----------------------------------------------------------------------")

querystring = {"requestType": "stopForging", "adminPassword": "1"}
response = requests.request("POST", url26, params=querystring)
print(response.text)
print("----------------------------------------------------------------------")

querystring = {"requestType": "stopForging", "adminPassword": "1"}
response = requests.request("POST", url27, params=querystring)
print(response.text)
print("----------------------------------------------------------------------")

querystring = {"requestType": "stopForging", "adminPassword": "1"}
response = requests.request("POST", url28, params=querystring)
print(response.text)
print("----------------------------------------------------------------------")

querystring = {"requestType": "stopForging", "adminPassword": "1"}
response = requests.request("POST", url29, params=querystring)
print(response.text)
print("----------------------------------------------------------------------")





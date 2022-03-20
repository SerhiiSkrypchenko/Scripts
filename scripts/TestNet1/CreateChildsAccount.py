import json

import requests
import random

import simplejson as simplejson

import data
import time
import testNet2
import testNet3
import testNet1
import testNet4_tap
URL = testNet3.t3

parentAccount =  "USDS-X5JH-TJKJ-DVGC-5T2V8"
psecret = "1"
node = random.choice(URL)

headers = {
            'Content-Type': "application/json"
        }

data = {
        'parent': parentAccount,
        'secret': psecret,
        'child_secret_list': ["100000","100001"]
}
print(node)
response = requests.request("POST",
                                    node + "/rest/v2/account/test",
                                    headers=headers, json = data)
print(response.json())
tx = response.json()["tx"]
print(tx)
data = {"tx": str(tx)}
response = requests.request("POST",
                                    node + "/rest/v2/transaction", headers = headers,
                                    json =  data
                                    )
print(response.json())












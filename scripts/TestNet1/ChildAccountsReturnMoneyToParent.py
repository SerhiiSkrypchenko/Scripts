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
URL = testNet3.t3_apl

parentAccount =  "APL-X5JH-TJKJ-DVGC-5T2V8"
psecret = "1"
node = random.choice(URL)
accountReceive = "APL-X5JH-TJKJ-DVGC-5T2V8"

headers = {
            'Content-Type': "application/json"
        }




for k in range(100000, 100500, 1):
        node = random.choice(URL)
        print(" <<<< --- START ---- >>>> ")
        print(" <<<<<<< --------- " + node + " ----- >>>>>>>")

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
        response = requests.request("GET",
                                    "http://" + node + "/apl",
                                    params=getAccountId)

        accountSender = response.json()["accountRS"]
        sender = response.json()["account"]
        print("sender secret phrase = " + str(k))
        print("accountSender = " + accountSender)

        getAccountSender = {"": "%2Fapl", "requestType": "getAccount", "account": sender}
        response = requests.request("GET", "http://" + node + "/apl", params=getAccountSender)
        print(response.json())
        balanceSenderAccount = response.json()['unconfirmedBalanceATM']
        print(balanceSenderAccount)

        amountATM = int(balanceSenderAccount) - 100000000
        print("amountATM = " + str(amountATM))

        headers = {
            'Content-Type': "application/json"
        }

        data = {'parent': parentAccount, 'psecret': psecret, 'sender': str(accountSender), 'csecret': str(k),'recipient':accountReceive, 'amount':str(amountATM)}

        response = requests.request("POST",
                                    "http://" + node + "/rest/v2/account/money",
                                    headers=headers, json = data)
        print(response.json())
        print(response.status_code)
        tx = response.json()["tx"]
        print(tx)
        data = {"tx": str(tx)}
        response = requests.request("POST",
                                    "http://" + node + "/rest/v2/transaction", headers = headers,
                                    json =  data
                                    )
        print(response.json())
        print("recipient = " + response.json()["recipient"])
        print("sender = " + response.json()["sender"])
        print("----------- END -------------")
        print()
        time.sleep(0)











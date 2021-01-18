import requests
import random
import data
import time
import testNet2
import testNet3
import testNet1
accountReceive = "REC"
duration = 15
messageToEncrypt = "{\"type\": \"REQUEST_MIXING\", \"epicId\": \"" + accountReceive + "\", \"approximateMixingDuration\": \"" + str(duration) + "\"}"
print(str(messageToEncrypt))

amountATM = "3000" # 2000 APL
amount = amountATM+"00000000"
print(amount)
duration = 15
limit = 100
j = 1
i = 100000000000
amount = 0
fee_APL = 500000000
# p = random.randint(1, 100)
print(" <<<< --- START ---- >>>> " + str(j))
t1 = random.choice(testNet3.mixer)
# p = random.randint(1, 200)
p = "mixer"
# print(" <<<<<<< --------- " + t1 + " ----- >>>>>>>")
getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": p}
response = requests.request("GET", "http://" + t1 + "/apl",
                            params=getAccountId)
# print(response.json())
accountReceive = response.json()["accountRS"]
print(str("accountReceive #" + str(j) + " = " + accountReceive))
print("secretPhrase of accountReceive is " + str(i))
print("--------------------------")
account = response.json()["account"]

getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
response = requests.request("GET",
                            "http://" + t1 + "/apl",
                            params=getAccountId)
accountSender = response.json()["accountRS"]
sender = response.json()["account"]
print("accountSender = " + accountSender)
print("id of account sender = " + sender)
print("secretPharse of account Sender is " + str(p))

getAccount = {"": "%2Fapl", "requestType": "getAccount", "account": sender}
response = requests.request("GET",
                            "http://" + t1 + "/apl",
                            params=getAccount)
balance = response.json()["balanceATM"]
APL = int(balance) - fee_APL

print("balance of SENDER = " + balance)
print("APL for sending = " + str(APL))
print("-------------------------")


#t1 = random.choice(testNet3.mixer)
#response = requests.request("GET", "https://wallet.testnet3.apollowallet.org/mixer")
#print(response.json())
#id = response.json()["id"]
#print("id = " + str(id))
#recipientMixer = response.json()["rsId"]
#print("recipientMixer = " + recipientMixer)
#recipientMixerPublicKey = response.json()["publicKey"]
#print("recipientMixerPublicKey = " + recipientMixerPublicKey)
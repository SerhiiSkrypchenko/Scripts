import requests
import random
import data
import time
import testNet2
import testNet3
import testNet1



duration = 240
limit = 300
j = 1
i = 100000000000
amount = 0
fee_APL = 500000000
while (j<=limit):

    #p = random.randint(1, 100)
    print(" <<<< --- START ---- >>>> " + str(j))
    t1 = random.choice(testNet2.mixer)
    #p = random.randint(1, 200)
    p = "504"
    #print(" <<<<<<< --------- " + t1 + " ----- >>>>>>>")
    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": p}
    response = requests.request("GET", "http://" + t1 + "/apl",
                                params=getAccountId)
    #print(response.json())
    accountReceive = response.json()["accountRS"]
    print(str("accountReceive #" + str(j) + " = " + accountReceive))
    print("secretPhrase of accountReceive is " + p)
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
    print("secretPharse of account Sender is " + str(i))

    getAccount = {"": "%2Fapl", "requestType": "getAccount", "account": sender}
    response = requests.request("GET",
                                "http://" + t1 + "/apl",
                                params=getAccount)
    balance = response.json()["balanceATM"]
    APL = int(balance) - fee_APL

    print("balance of SENDER = " + balance)
    print("APL for sending = " + str(APL))
    print("-------------------------")
    response = requests.request("GET", "https://apl-t2-2.testnet2.apollowallet.org/mixer")
    #response = requests.request("GET", "https://wallet.testnet3.apollowallet.org/mixer")

    id = response.json()["id"]
    print("id = " + str(id))
    recipientMixer = response.json()["rsId"]
    print("recipientMixer = " + recipientMixer)
    recipientMixerPublicKey = response.json()["publicKey"]
    print("recipientMixerPublicKey = " + recipientMixerPublicKey)
    print("--------------------------")

    messageToEncrypt = "{\"type\": \"REQUEST_MIXING\", \"epicId\": \"" + accountReceive + "\", \"approximateMixingDuration\": \"" + str(duration) + "\"}"
    response = requests.request("POST",
                                "http://" + t1 + "/apl",
                                params=data.sendMoneyPrivateMixer(recipientMixer, recipientMixerPublicKey, str(APL), str(i), sender, str(duration), messageToEncrypt))

    print("MIXER RESPONSE IS: ")
    print(response.json())
    #print(response.json())

    # print(" <<<<<<< --------- " + t1 + " ----- >>>>>>>")
    print("----------- END -------------")
    time.sleep(0)
    amount = amount + APL
    i += 1
    j += 1
print("TOTAL APL SENDING IS - > " + str(amount))










import requests
import random
import data
import time
import testNet2
import testNet3
import testNet1

amountATM = "1000" # quantity of APL

duration = 10080
limit = 300
j = 1
i = 200000000000

while (j<=limit):

    #p = random.randint(1, 100)
    print(" <<<< --- START ---- >>>> " + str(j))
    t1 = random.choice(testNet1.mixer)
    #p = random.randint(1, 200)
    p = "mixer7days"
    #print(" <<<<<<< --------- " + t1 + " ----- >>>>>>>")
    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
    response = requests.request("GET", "http://" + t1 + "/apl",
                                params=getAccountId)
    #print(response.json())
    accountReceive = response.json()["accountRS"]

    print(str("accountReceive #" + str(j) + " = " + accountReceive))
    print("secretPhrase of accountReceive is " + str(i))
    print("--------------------------")
    account = response.json()["account"]

    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
    response = requests.request("GET",
                                "http://" + t1 + "/apl",
                                params=getAccountId)

    accountSender = response.json()["accountRS"]
    sender = response.json()["account"]

    print("accountSender = " + accountSender)
    print("id of account sender = " + sender)
    print("secretPharse of account Sender is " + str(p))
    print("-------------------------")

    response = requests.request("GET", "https://apl-t1-1.testnet.apollowallet.org/mixer")
    #response = requests.request("GET", "https://apl-t2-2.testnet2.apollowallet.org/mixer")
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
                                "https://" + t1 + "/apl",
                                params=data.sendMoneyPrivateMixer(recipientMixer, recipientMixerPublicKey, amountATM+"00000000", str(p), sender, str(duration), messageToEncrypt))

    print("MIXER RESPONSE IS: ")
    print(response.json())
    #print(response.json())

    # print(" <<<<<<< --------- " + t1 + " ----- >>>>>>>")
    print("----------- END -------------")
    time.sleep(2)
    i += 1
    j += 1











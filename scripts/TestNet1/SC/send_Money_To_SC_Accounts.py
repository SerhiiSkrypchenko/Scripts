import testNet3
import requests
import random
import testNet2
import testNet1

publisher = "APL-GT9X-LHFA-S7XQ-AM6F6"
secretPhrasePublisher = "sc1"
publisherHash = "0x82349393da8764fd"

receiver = "APL-YN7W-EXQF-6PLH-52SXK"
receiverHash = "'0x38f700676cdf50bc'"
secretPhraseReceiver = "sbank"

spender = "APL-MU39-U3F5-24E4-DLBWJ"
spenderHash = "'0xb87132d05a39e827'"
secretPhraseSpender = "spender"

account1 = "APL-ST32-2HTL-UGA6-HNFFP"
secretPhraseAccount1 = "sc2"

fee_APL = 100000000
url = random.choice(testNet2.t2)
apl_Amount = 20000000000000000

def sendMoney(recipient, amountATM, secretPhrase, feeATM, sender):
    return {"requestType": "sendMoney", "recipient": recipient, "amountATM": amountATM,
            "secretPhrase": secretPhrase, "feeATM": feeATM, "deadline": "1440",
            "sender": sender}

response = requests.request("POST",
                                url + "/apl",
                                params=sendMoney(str(publisher),
                                                             str(apl_Amount),
                                                             "0",
                                                             str(fee_APL),
                                                             "9211698109297098287"))
print(response.json())
response = requests.request("POST",
                                url + "/apl",
                                params=sendMoney(str(receiver),
                                                             str(apl_Amount),
                                                             "0",
                                                             str(fee_APL),
                                                             "9211698109297098287"))
print(response.json())
response = requests.request("POST",
                                url + "/apl",
                                params=sendMoney(str(spender),
                                                             str(apl_Amount),
                                                             "0",
                                                             str(fee_APL),
                                                             "9211698109297098287"))
print(response.json())
response = requests.request("POST",
                                url + "/apl",
                                params=sendMoney(str(account1),
                                                             str(apl_Amount),
                                                             "0",
                                                             str(fee_APL),
                                                             "9211698109297098287"))
print(response.json())
import requests
import random
import time
import config_Luna_Wallet


url = config_Luna_Wallet.xln_t1

secondSecretPhrase = "failed2"
firstSecretPhrase = "failed1"
firstAccount = "XLN-WFZU-5KTN-UNU3-8X2TV"
firstAccountId = "7918486052854970362"
secondAccount = "XLN-7H8W-5TK3-E58Y-82F8Y"
secondAccountId = "8005605864982625500"

print("secret phrase of first acc is : " + firstSecretPhrase)
print("secret phrase of second acc is : " + secondSecretPhrase)

#"add_message": True,
#"messageToEncrypt": "test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long"


def sendMoney(recipient, amountMLN, secretPhrase, feeMLN):
    return {"requestType": "sendMoney", "recipient": recipient, "amountMLN": amountMLN,
            "secretPhrase": secretPhrase, "feeMLN": feeMLN, "deadline": "1440"
            }

fee_MLN = 300000000
randomUrl = random.choice(url)
sec = 2


getAccountFirst = {"": "%2Fapl", "requestType": "getAccount", "account": firstAccountId}
response = requests.request("GET", randomUrl + "/xln-api", params=getAccountFirst)
print(response.json())
if "errorDescription" in response.text:
    response = requests.request("POST",
                                randomUrl + "/xln-api",
                                params=sendMoney(str(firstAccount),
                                                 str(2000000000000),
                                                        "0",
                                                 str(fee_MLN)
                                                 ))
    print(response.json())
else:
    balanceFirstAccount = response.json()['balanceMLN']
    print("balance of first account is " + balanceFirstAccount)

getAccountSecond = {"": "%2Fapl", "requestType": "getAccount", "account": secondAccount}
response = requests.request("GET", randomUrl + "/xln-api", params=getAccountSecond)
print(response.json())
if "errorDescription" in response.text:
    """response = requests.request("POST",
                                randomUrl + "/xln-api",
                                params=sendMoneyPrivate(str(accountReceive),
                                                        str(200000000000000),
                                                        "0",
                                                        str(fee_APL)
                                                        ))"""
    print(response.json())
else:
    balanceSecondAccount = response.json()["balanceMLN"]
    print("balance of second account is " + balanceSecondAccount)
time.sleep(20)
alive = True
while alive:
    print(" <<<< --- START ---- >>>> ")
    randomUrl = random.choice(url)

    getAccountFirst = {"": "%2Fapl", "requestType": "getAccount", "account": firstAccountId}
    response = requests.request("GET", randomUrl + "/xln-api", params=getAccountFirst)
    base_MLN_AMOUNT = int(response.json()['balanceMLN'])

    response = requests.request("POST",
                                randomUrl + "/xln-api",
                                params=sendMoney(str(secondAccount),
                                                 str(base_MLN_AMOUNT - fee_MLN),
                                                 firstSecretPhrase,
                                                 str(fee_MLN)
                                                 ))
    print("TRANSACTION #1 from first -> second")
    print(response.json())
    response = requests.request("POST",
                                randomUrl + "/xln-api",
                                params=sendMoney(str(secondAccount),
                                                 str(base_MLN_AMOUNT - 2*fee_MLN),
                                                 firstSecretPhrase,
                                                 str(fee_MLN)
                                                 ))
    print("TRANSACTION #2 from first -> second")
    print(response.json())
    time.sleep(sec)
    getAccountSecond = {"": "%2Fapl", "requestType": "getAccount", "account": secondAccount}
    response = requests.request("GET", randomUrl + "/xln-api", params=getAccountSecond)
    base_MLN_AMOUNT = int(response.json()['balanceMLN'])

    response = requests.request("POST",
                                randomUrl + "/xln-api",
                                params=sendMoney(str(firstAccount),
                                                 str(base_MLN_AMOUNT - fee_MLN),
                                                 secondSecretPhrase,
                                                 str(fee_MLN)
                                                 ))
    print("TRANSACTION #1 from second -> first")
    print(response.json())
    response = requests.request("POST",
                                randomUrl + "/xln-api",
                                params=sendMoney(str(firstAccount),
                                                 str(base_MLN_AMOUNT - fee_MLN - fee_MLN),
                                                 secondSecretPhrase,
                                                 str(fee_MLN)
                                                 ))
    print("TRANSACTION #2 from second -> first")
    print(response.json())
    print("<<<< ---- END ---- >>>>")
    time.sleep(sec)

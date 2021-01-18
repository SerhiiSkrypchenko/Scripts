import requests

"""from sys import argv

script, first, second, third = argv

print ("Этот скрипт называется: ", script)
print("он предназначен для рассылки денег с генезис аккаунта с секрет фразой 0 на другие аккаунты")
print ("секрет фраза первого аккаунта на который отправлять деньги: ", first)
print ("секрет фраза второго аккаунта на который отправлять деньги: ", second)
print ("Сумма аполло для отправки на каждый аккаунт: ", third)"""

npz_account = "APL-NZKH-MZRE-2CTT-98NPZ"
npz_sender = "9211698109297098287"
npz_secret_phrase = "0"

#URL = "localhost:7876"
URL = "apl-t2-1.testnet2.apollowallet.org"



#start = first
#finish = second
#amountATM = str(third) + "00000000"
start = 100000
finish = 100100
amountATM = "100000000000"
print(amountATM)


def sendMoneyToManyAccounts(url, finishNumber, startNumber):
    for k in range(int(startNumber), int(finishNumber) + 1, 1):
        print(k)
        print(" ----- SEND MONEY TO >>> " + str(k) + " <<<---- ACCOUNT --- ")
        headers = {
            'Content-Type': "application/json"
        }
        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
        response = requests.request("GET", "http://" + url + "/apl", headers=headers, params=getAccountId)
        print(response.json())
        account = response.json()["accountRS"]
        print("---- RECIPIENT ---- >>>> " + str(account))

        data = {"requestType": "sendMoney", "recipient": str(account), "amountATM": amountATM,
            "secretPhrase": npz_secret_phrase, "feeATM": "100000000", "deadline": "1440",
            "sender": npz_sender}
        response = requests.request("POST", "http://" + url + "/apl",
                                    headers=headers,
                                    params=data)
        print(response.json())
        print("<<< -------- >>> FINISHED <<< ---------->>> ")

sendMoneyToManyAccounts(URL, finish, start)





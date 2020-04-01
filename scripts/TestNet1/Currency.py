import testNet2
import requests
import random
import string
import conf
from exchangeFunctions import vaults
import testNet3

def id_generator(size=5, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

def issueVaultCurrency(url, feeATM, sender, passphrase):
    initialSupply = random.randint(10, 10000)
    print("initialSupply = " + str(initialSupply))
    type = random.choice([1, 3])
    print("type = " + str(type))
    param = {'requestType': 'issueCurrency',
             'name': id_generator(5) + "123",
             'code': id_generator(3),
             'description': "Vault " + str(id_generator(18)) + " KILL SHARDING                                                                             ';:.,<>/?][{}\|=+-_)(*&^%$#@!~*-+?:;" "                      THE END              ",
             'type': type,
             'initialSupply': initialSupply,
             'maxSupply': initialSupply,
             'feeATM': feeATM,
             'sender': sender,
             'passphrase': passphrase,
             'reserveSupply': 0,
             'deadline': 1440
             }
    # randomUrl = random.choice(url)
    response = requests.post("http://" + url + "/apl", param)
    print(response.json())
    return response

def issueStandardCurrency(url, feeATM, secretPhrase):
    initialSupply = random.randint(10, 10000)
    print("initialSupply = " + str(initialSupply))
    type = random.choice([1, 3])
    print("type = " + str(type))
    param = {'requestType': 'issueCurrency',
             'name': id_generator(5),
             'code': id_generator(3),
             'description': "Standard " + str(id_generator(18)),
             'type': type,
             'initialSupply': initialSupply,
             'maxSupply': initialSupply,
             'feeATM': feeATM,
             #'sender': sender,
             'secretPhrase': secretPhrase,
             'reserveSupply': 0,
             'deadline': 1440
             }
    # randomUrl = random.choice(url)
    response = requests.post("http://" + url + "/apl", param)
    print(response.json())
    return response


<<<<<<< Updated upstream

issueStandardCurrency(testNet2.peer2,
              4000000000000,
              "APL-NZKH-MZRE-2CTT-98NPZ",
              "0")
=======
while True:
    url = random.choice(testNet2.peer1)
    for i in range(0, len(vaults)):
        account = vaults[i].account
        print("ACCOUNT = " + str(account))
        sender = vaults[i].sender
        passphrase = vaults[i].passPhrase
        issueVaultCurrency(url,
                            4000000000000,
                            account,
                            passphrase)
        issueStandardCurrency(url,
                            4000000000000,
                            str(i))
>>>>>>> Stashed changes

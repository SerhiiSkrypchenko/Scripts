import testNet2
import requests
import random
import string

def id_generator(size=5, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

def issueVaultCurrency(url, feeATM, sender, passphrase):
    initialSupply = random.randint(10, 10000)
    print("initialSupply = " + str(initialSupply))
    type = random.choice([1, 3])
    print("type = " + str(type))
    param = {'requestType': 'issueCurrency',
             'name': id_generator(5),
             'code': id_generator(3),
             'description': "Vault " + str(id_generator(18)),
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

def issueStandardCurrency(url, feeATM, sender, secretPhrase):
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
             'sender': sender,
             'secretPhrase': secretPhrase,
             'reserveSupply': 0,
             'deadline': 1440
             }
    # randomUrl = random.choice(url)
    response = requests.post("http://" + url + "/apl", param)
    print(response.json())
    return response



issueStandardCurrency(testNet2.localhost,
              4000000000000,
              "APL-NZKH-MZRE-2CTT-98NPZ",
              "0")
import requests
import json
import testNet3
import time
import random
import testNet2
#url = random.choice(testNet2.t2)
url = "https://sc.t2.apollowallet.org"
publish = "/rest/v2/smc/publish/multisig"
broadcast = "/rest/v2/transaction"
call = "/rest/v2/smc/method/call"
read = "/rest/v2/smc/method/read"

#constructor(name, symbol, cap, initialSupply, rate, releaseDelay, vault)
#depositOf   (address 1 = payee, address 2 = token)
type = "MyAPL20PersonalLockable"
type_escrow = "MyTokenEscrow"
source = "class MyAPL20PersonalLockable extends APL20PersonalLockable {\n      constructor(){\n          super('New','New','2000000000000','0','100000000','0','0x82349393da8764fd');\n      }\n    }"
source_1 = "class MyAPL20PersonalLockable extends APL20PersonalLockable {\n      constructor(){\n          super('New1','New1','2000000000000','0','100000000','0','0x82349393da8764fd');\n      }\n    }"
source_2 = "class MyAPL20PersonalLockable extends APL20PersonalLockable {\n      constructor(){\n          super('New2','New2','2000000000000','10000000000','10000000','0','0x38f700676cdf50bc');\n      }\n    }"
source_3 = "class MyAPL20PersonalLockable extends APL20PersonalLockable {\n      constructor(){\n          super('New3','New3','2000000000000','20000000000','1000000','0','0x82349393da8764fd');\n      }\n    }"
source_4 = "class MyAPL20PersonalLockable extends APL20PersonalLockable {\n      constructor(){\n          super('New4','New4','2000000000000','30000000000','100000','0','0x82349393da8764fd');\n      }\n    }"
source_Escrow = "class MyTokenEscrow extends TokenEscrow {\n      constructor(){\n          super();\n      }\n    }"

npz_account = ""
npz_accountHash = "'0x7fd6869feeca7e2f'"

publisher = "APL-GT9X-LHFA-S7XQ-AM6F6"
secretPhrasePublisher = "sc1"
publisherHash = "'0x82349393da8764fd'"

"""publisher = "APL-NQNJ-KHMR-4Y4Z-AWR3P"
secretPhrasePublisher = "1000"
publisherHash = "'0x82349393da8764fd'"""


account1 = "APL-ST32-2HTL-UGA6-HNFFP"
secretPhraseAccount1 = "sc2"

receiver = "APL-YN7W-EXQF-6PLH-52SXK"
receiverHash = "'0x38f700676cdf50bc'"
secretPhraseReceiver = "sbank"

spender = "APL-MU39-U3F5-24E4-DLBWJ"
spenderHash = "'0xb87132d05a39e827'"
secretPhraseSpender = "spender"


buy = "buy"
unlock = "unlock"
transfer = "transfer"
burn = "burn"
freeze = "freeze"
unfreeze = "unfreeze"
approve = "approve"
transfer_From = "transferFrom"

transferATM = "7000000000"
freeze_Tokens = "2000000000"
approve_Tokens = "15000000000"

basic_params = [
            ""
        ]
transfer_params = [receiverHash, transferATM]
freeze_params = [freeze_Tokens]
approve_params = [spenderHash, approve_Tokens]
transferFrom_params = [publisherHash, receiverHash, approve_Tokens]
burn_params = [transferATM]

def create_sc(type, publisher, secretPhrase, source):
    # create SC functionality
    payload = json.dumps({
        "name": type,
        "sender": "Cvfhn-Cfhnsi3=Lee;tHjpev",
        "params": [],
        "value": 0,
        "fuelPrice": 10000,
        "fuelLimit": 500000000,
        "source": source,
        "secretPhrase": secretPhrase
    })
    headers = {
        'Content-Type': 'application/json'
    }
    print("Create SC")
    response = requests.request("POST", url + publish, headers=headers, data=payload)
    tx = response.json()["tx"]
    payload_broadcast = json.dumps({
        "tx": tx
    })
    response = requests.request("POST", url + broadcast, headers=headers, data=payload_broadcast)
    print(response.json())
    print("TxId = " + response.json()["transaction"])
    sc_Address = response.json()["transaction"]
    print("SC ADDRESS = " + response.json()["transaction"])
    print("Smart contract is created")
    #print("Waiting 60 sec")
    time.sleep(0)
    return sc_Address

def method(sc_Address, sender, secretPhrase, value, method_name, params):
    print("Start " + method_name)
    payload = json.dumps({
        "address": sc_Address,
        "sender": sender,
        "value": value,
        "fuelLimit": 500000000,
        "fuelPrice": 10000,
        "params": params,
        "secretPhrase": secretPhrase,
        "name": method_name
    })
    headers = {
        'Content-Type': 'application/json'
    }
    #url = random.choice(testNet2.t2)
    url = "https://sc.t2.apollowallet.org"
    print(url)
    call_response = requests.request("POST", url + call, headers=headers, data=payload)
    print(call_response.text)
    call_tx = call_response.json()["tx"]
    time.sleep(0)
    # broadcast buy tx
    payload_broadcast = json.dumps({
        "tx": call_tx
    })
    response = requests.request("POST", url + broadcast, headers=headers, data=payload_broadcast)
    print(response.json())
    print("END " + method_name)
    time.sleep(0)
    return response

def read_method(sc_Address, function, address_Hash_1, address_Hash_2):
    print("Start " + function)
    payload = json.dumps({
        "address": sc_Address,
        "members": [
            {
                "function": function,
                "input": [
                    address_Hash_1,
                    address_Hash_2
                ]
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    #url = random.choice(testNet2.t2)
    url = "https://sc.t2.apollowallet.org"
    print(url)
    call_response = requests.request("POST", url + read, headers=headers, data=payload)
    print(call_response.json())
    deposit_Amount = call_response.json()["results"][0]["output"][0]
    print("Deposit amount = " + deposit_Amount)
    print("Payee >>>" + address_Hash_1 + "<<< has >>> " + deposit_Amount + " <<<  amount of " + address_Hash_2 + " tokens on deposit on " + sc_Address +" escrow address")
    print("END " + function)
    return call_response

#read_method("APL-HE2N-4TZH-Z25A-F6GSE", "depositOf", "'0x7fd6869feeca7e2f'", "'0x82349393da8764fd'")

sc_Address = create_sc(type, publisher, secretPhrasePublisher, source)
sc_Address_1 = create_sc(type, publisher, secretPhrasePublisher, source_1)
sc_Address_2 = create_sc(type, publisher, secretPhrasePublisher, source_2)
sc_Address_3 = create_sc(type, publisher, secretPhrasePublisher, source_3)
sc_Address_4 = create_sc(type, publisher, secretPhrasePublisher, source_4)
#sc_Address_Escrow = create_sc(type_escrow, publisher, secretPhrasePublisher, source_Escrow)

"""sc_Address = "9936165364551841584"
sc_Address_1 = "4191720988775803599"
sc_Address_2 = "81912649030847372"
sc_Address_3 = "8575324660375887336"
sc_Address_4 = "14403425347709241951"""

print("Smart Contract Address = " + sc_Address)
print("Smart Contract Address 1 = " + sc_Address_1)
print("Smart Contract Address 2 = " + sc_Address_2)
print("Smart Contract Address 3 = " + sc_Address_3)
print("Smart Contract Address 4 = " + sc_Address_4)
time.sleep(50)
sec = 20

while True:
    method(sc_Address,publisher,secretPhrasePublisher,30000000000,buy,basic_params)
    method(sc_Address,account1,secretPhraseAccount1,40000000000, buy, basic_params)
    method(sc_Address_1, publisher, secretPhrasePublisher, 30000000000, buy, basic_params)
    method(sc_Address_1, account1, secretPhraseAccount1, 40000000000, buy, basic_params)
    method(sc_Address_2, publisher, secretPhrasePublisher, 30000000000, buy, basic_params)
    method(sc_Address_2, account1, secretPhraseAccount1, 40000000000, buy, basic_params)
    method(sc_Address_3, publisher, secretPhrasePublisher, 30000000000, buy, basic_params)
    method(sc_Address_3, account1, secretPhraseAccount1, 40000000000, buy, basic_params)
    method(sc_Address_4, publisher, secretPhrasePublisher, 30000000000, buy, basic_params)
    method(sc_Address_4, account1, secretPhraseAccount1, 40000000000, buy, basic_params)
    print("")
    time.sleep(sec)

    method(sc_Address,publisher,secretPhrasePublisher,0,unlock,basic_params)
    method(sc_Address, account1, secretPhraseAccount1, 0, unlock, basic_params)
    method(sc_Address_1, publisher, secretPhrasePublisher, 0, unlock, basic_params)
    method(sc_Address_1, account1, secretPhraseAccount1, 0, unlock, basic_params)
    method(sc_Address_2, publisher, secretPhrasePublisher, 0, unlock, basic_params)
    method(sc_Address_2, account1, secretPhraseAccount1, 0, unlock, basic_params)
    method(sc_Address_3, publisher, secretPhrasePublisher, 0, unlock, basic_params)
    method(sc_Address_3, account1, secretPhraseAccount1, 0, unlock, basic_params)
    method(sc_Address_4, publisher, secretPhrasePublisher, 0, unlock, basic_params)
    method(sc_Address_4, account1, secretPhraseAccount1, 0, unlock, basic_params)
    print("")
    time.sleep(sec)

    method(sc_Address, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_1, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_1, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_1, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_1, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_1, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_1, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_1, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_1, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_1, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_1, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_1, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_1, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_1, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_1, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_1, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_1, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_2, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_2, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_2, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_2, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_2, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_2, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_2, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_2, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_2, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_2, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_2, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_2, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_2, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_2, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_2, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_2, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_3, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_3, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_3, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_3, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_3, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_3, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_3, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_3, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_3, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_3, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_3, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_3, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_3, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_3, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_3, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_3, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_4, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_4, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_4, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_4, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_4, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_4, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_4, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_4, publisher, secretPhrasePublisher, 0, transfer, transfer_params)
    method(sc_Address_4, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_4, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_4, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_4, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_4, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_4, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_4, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    method(sc_Address_4, account1, secretPhraseAccount1, 0, transfer, transfer_params)
    print("")
    time.sleep(sec)

    method(sc_Address, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address_1, publisher, secretPhrasePublisher, 0, burn, burn_params)
    method(sc_Address_1, publisher, secretPhrasePublisher, 0, burn, burn_params)
    method(sc_Address_1, publisher, secretPhrasePublisher, 0, burn, burn_params)
    method(sc_Address_1, publisher, secretPhrasePublisher, 0, burn, burn_params)
    method(sc_Address_1, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address_1, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address_1, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address_1, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address_2, publisher, secretPhrasePublisher, 0, burn, burn_params)
    method(sc_Address_2, publisher, secretPhrasePublisher, 0, burn, burn_params)
    method(sc_Address_2, publisher, secretPhrasePublisher, 0, burn, burn_params)
    method(sc_Address_2, publisher, secretPhrasePublisher, 0, burn, burn_params)
    method(sc_Address_2, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address_2, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address_2, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address_2, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address_3, publisher, secretPhrasePublisher, 0, burn, burn_params)
    method(sc_Address_3, publisher, secretPhrasePublisher, 0, burn, burn_params)
    method(sc_Address_3, publisher, secretPhrasePublisher, 0, burn, burn_params)
    method(sc_Address_3, publisher, secretPhrasePublisher, 0, burn, burn_params)
    method(sc_Address_3, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address_3, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address_3, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address_3, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address_4, publisher, secretPhrasePublisher, 0, burn, burn_params)
    method(sc_Address_4, publisher, secretPhrasePublisher, 0, burn, burn_params)
    method(sc_Address_4, publisher, secretPhrasePublisher, 0, burn, burn_params)
    method(sc_Address_4, publisher, secretPhrasePublisher, 0, burn, burn_params)
    method(sc_Address_4, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address_4, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address_4, account1, secretPhraseAccount1, 0, burn, burn_params)
    method(sc_Address_4, account1, secretPhraseAccount1, 0, burn, burn_params)

    method(sc_Address_1, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address_1, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address_1, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address_1, receiver, secretPhraseReceiver, 0, burn, burn_params)

    method(sc_Address_2, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address_2, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address_2, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address_2, receiver, secretPhraseReceiver, 0, burn, burn_params)

    method(sc_Address_3, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address_3, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address_3, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address_3, receiver, secretPhraseReceiver, 0, burn, burn_params)

    method(sc_Address_4, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address_4, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address_4, receiver, secretPhraseReceiver, 0, burn, burn_params)
    method(sc_Address_4, receiver, secretPhraseReceiver, 0, burn, burn_params)
    print("")
    time.sleep(sec)



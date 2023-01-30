import requests
import json
import testNet3
import time

url = testNet3.peer1

publish = "/rest/v2/smc/publish"
broadcast = "/rest/v2/transaction"
call = "/rest/v2/smc/method/call"

#constructor(name, symbol, cap, initialSupply, rate, releaseDelay, vault)

type_escrow = "MyTokenEscrow"
source_Escrow = "class MyTokenEscrow extends TokenEscrow {\n      constructor(){\n          super();\n      }\n    }"
npz_account = ""
npz_accountHash = "'0x7fd6869feeca7e2f'"

publisher = "APL-GT9X-LHFA-S7XQ-AM6F6"
secretPhrasePublisher = "sc1"
publisherHash = "'0x82349393da8764fd'"

account1 = "APL-ST32-2HTL-UGA6-HNFFP"
secretPhraseAccount1 = "sc2"

receiver = "APL-YN7W-EXQF-6PLH-52SXK"
receiverHash = "'0x38f700676cdf50bc'"
secretPhraseReceiver = "sbank"

spender = "APL-MU39-U3F5-24E4-DLBWJ"
spenderHash = "'0xb87132d05a39e827'"
secretPhraseSpender = "spender"

withdraw = "withdraw"
deposit = "deposit"
buy = "buy"
unlock = "unlock"
transfer = "transfer"
burn = "burn"
freeze = "freeze"
unfreeze = "unfreeze"
approve = "approve"
transfer_From = "transferFrom"

transferATM = "7000000000"
freeze_Tokens = "20000000000"
approve_Tokens = "15000000000"

basic_params = [
            ""
        ]
transfer_params = [receiverHash, transferATM]
freeze_params = [freeze_Tokens]
approve_params = [spenderHash, approve_Tokens]
transferFrom_params = [publisherHash, receiverHash, approve_Tokens]
deposit_params = [npz_accountHash,npz_accountHash,"5000000000"]
withdraw_params = [npz_accountHash, npz_accountHash]

def create_sc(type, publisher, secretPhrase, source):
    # create SC functionality
    payload = json.dumps({
        "name": type,
        "sender": publisher,
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
    print(response.json())
    tx = response.json()["tx"]
    payload_broadcast = json.dumps({
        "tx": tx
    })
    response = requests.request("POST", url + broadcast, headers=headers, data=payload_broadcast)
    print(response.json())
    print("TxId = " + response.json()["transaction"])
    sc_Address = response.json()["recipient"]
    print("SC ADDRESS = " + response.json()["recipient"])
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

sc_Address_Escrow = create_sc(type_escrow, publisher, secretPhrasePublisher, source_Escrow)
#sc_Address_Escrow = "APL-K4MH-S6E8-994G-39AKC"
print("SC address = " + sc_Address_Escrow)
time.sleep(20)
method(sc_Address_Escrow,publisher,secretPhrasePublisher,0,deposit,deposit_params)
time.sleep(20)
method(sc_Address_Escrow,publisher,secretPhrasePublisher,0,withdraw,withdraw_params)






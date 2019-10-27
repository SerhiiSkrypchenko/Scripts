localhost = "http://localhost:7876/apl"

payload = ""
headers = {
    'Content-Type': "application/json"
}


def sendMoneyFromVaultWalletToSandardWallet(recipient, amountATM, passPhrase, feeATM, sender):
    return {"requestType": "sendMoney", "recipient": recipient, "amountATM": amountATM,
            "passphrase": passPhrase, "feeATM": feeATM, "deadline": "1440",
            "sender": sender}


def sendMoneyFromStandardWalletToVaultWallet(recipient, amountATM, secretPhrase, feeATM, sender):
    return {"requestType": "sendMoney", "recipient": recipient, "amountATM": amountATM,
            "secretPhrase": secretPhrase, "feeATM": feeATM, "deadline": "1440",
            "sender": sender}


def sendMoneyReferenced(recipient, amountATM, secretPhrase, feeATM, sender, referencedTransactionFullHash):
    return {"requestType": "sendMoney", "recipient": recipient, "amountATM": amountATM,
            "secretPhrase": secretPhrase, "feeATM": feeATM, "deadline": "1440",
            "sender": sender, "referencedTransactionFullHash": referencedTransactionFullHash}


def sendMoneyPhased(recipient, amountATM, secretPhrase, feeATM, sender, phasingFinishHeight):
    return {"requestType": "sendMoney", "recipient": recipient, "amountATM": amountATM,
            "secretPhrase": secretPhrase, "feeATM": feeATM, "deadline": "1440",
            "sender": sender, "phasingFinishHeight": phasingFinishHeight, "phased": "true", "phasingVotingModel": "1",
            "phasingQuorum": "1"}

def sendMoney_Phased_Referenced(recipient, amountATM, secretPhrase, feeATM, sender, phasingFinishHeight, referencedTransactionFullHash):
    return {"requestType": "sendMoney", "recipient": recipient, "amountATM": amountATM,
            "secretPhrase": secretPhrase, "feeATM": feeATM, "deadline": "1440",
            "sender": sender, "phasingFinishHeight": phasingFinishHeight, "phased": "true", "phasingVotingModel": "1",
            "phasingQuorum": "1", "referencedTransactionFullHash": referencedTransactionFullHash, "messageIsPrunable": True}

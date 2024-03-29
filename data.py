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

def sendMoneyMultiSignature(recipient, amount, csecret, sender, parent, psecret):
    return {"recipient": recipient, "amount": amount,
            "csecret": csecret, "parent": parent, "psecret": psecret,
            "sender": sender}

def sendMoneyPrivate(recipient, amountATM, secretPhrase, feeATM, sender):
    return {"requestType": "sendMoneyPrivate", "recipient": recipient, "amountATM": amountATM,
            "secretPhrase": secretPhrase, "feeATM": feeATM, "deadline": "1440",
            "sender": sender}

def sendMoney(recipient, amountATM, secretPhrase, feeATM, sender):
    return {"requestType": "sendMoney", "recipient": recipient, "amountATM": amountATM,
            "secretPhrase": secretPhrase, "feeATM": feeATM, "deadline": "1440",
            "sender": sender}

def sendMoneyPrivateMixer(recipientMixer, mixerPublicKey, amountATM, secretPhrase, sender, duration, messageToEncrypt):
    return {"requestType": "sendMoneyPrivate", "recipient": recipientMixer, "amountATM": amountATM,
            "secretPhrase": secretPhrase, "feeATM": "500000000", "deadline": "1440",
            "sender": sender, "mixerPublicKey": mixerPublicKey, "isMixer": "true", "duration": duration,
            "isCustomFee": "true", "recipientPublicKey": mixerPublicKey,
            "messageToEncrypt": messageToEncrypt}

def sendMoneyReferenced(recipient, amountATM, secretPhrase, feeATM, sender, referencedTransactionFullHash):
    return {"requestType": "sendMoney", "recipient": recipient, "amountATM": amountATM,
            "secretPhrase": secretPhrase, "feeATM": feeATM, "deadline": "1440",
            "sender": sender, "referencedTransactionFullHash": referencedTransactionFullHash}

def sendMoneyPhased(recipient, amountATM, secretPhrase, feeATM, sender, phasingFinishHeight):
    return {"requestType": "sendMoney", "recipient": recipient, "amountATM": amountATM,
            "secretPhrase": secretPhrase, "feeATM": feeATM, "deadline": "20",
            "sender": sender, "phasingFinishHeight": phasingFinishHeight, "phased": "true", "phasingVotingModel": "1",
            "phasingQuorum": "1"}

def sendMoney_Phased_Referenced(recipient, amountATM, secretPhrase, feeATM, sender, phasingFinishHeight, referencedTransactionFullHash):
    return {"requestType": "sendMoney", "recipient": recipient, "amountATM": amountATM,
            "secretPhrase": secretPhrase, "feeATM": feeATM, "deadline": "30",
            "sender": sender, "phasingFinishHeight": phasingFinishHeight, "phased": "true", "phasingVotingModel": "1",
            "phasingQuorum": "1", "referencedTransactionFullHash": referencedTransactionFullHash, "messageIsPrunable": True,
            "add_message": True,
            "messageToEncrypt": "test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long"
            }

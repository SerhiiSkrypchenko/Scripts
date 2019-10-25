import requests


import data
import conf

response = requests.request("POST", data.localhost, data=data.payload, headers=data.headers,
                            params=data.sendMoneyFromVaultWalletToSandardWallet(conf.account1, "10000000000",
                                                                                conf.account2PassPhrase, "200000000",
                                                                                conf.sender2))
print(response.text)
response = requests.request("POST", data.localhost, data=data.payload, headers=data.headers,
                            params=data.sendMoneyFromStandardWalletToVaultWallet(conf.account2, "10000000000",
                                                                                 conf.account1SecretPhrase, "200000000",
                                                                                 conf.sender1))
print(response.json())
jsonData = response.json()
fullHash = jsonData.fullHash
print(fullHash)

import requests
import random

# Test Net 3
url31 = "http://51.15.250.32/rest/dex/offer"
url32 = "http://51.15.253.171/rest/dex/offer"
url33 = "http://51.15.210.116/rest/dex/offer"
url34 = "http://51.15.242.197/rest/dex/offer"
url35 = "http://51.15.218.241/rest/dex/offer"
urls3 = random.choice([url32, url33, url34, url35])
# Test Net 2
localhost = "http://localhost:7876/rest/dex/offer"
url21 = "http://51.15.247.49/rest/dex/offer"
url22 = "http://51.15.209.252/rest/dex/offer"
url23 = "http://51.15.228.90/rest/dex/offer"
url24 = "http://51.15.228.126/rest/dex/offer"
url25 = "http://51.15.228.171/rest/dex/offer"
url26 = "http://51.15.46.25/rest/dex/offer"
url27 = "http://51.15.72.23/rest/dex/offer"
url28 = "http://51.15.100.44/rest/dex/offer"
url29 = "http://51.15.233.93/rest/dex/offer"
# urls2 = random.choice([url21, url22, url23, url24, url25, url26, url27, url28, url29])
urls2 = random.choice([localhost])
headers = {
    'Content-Type': "application/x-www-form-urlencoded"

}
alive = True
while alive:
    print("--------------------------- BUY APL for ETH ---------------------------------")
    payload = "offerType=0&pairCurrency=1&pairRate=100000&offerAmount=1000000000000&sender=7821792282123976600" \
              "&passphrase" \
              "=11&feeATM=200000000&amountOfTime=86400&walletAddress=0x3d81757ee49fda2af1b63ee8eb7ffa67ab4ef0ee"
    response = requests.request("POST", urls3, headers=headers, data=payload)
    print(response.text)
    transaction1 = response.json()["transaction"]
    print("-----------------------------------------------------------------------------")
    print("--------------------------- BUY APL for ETH ---------------------------------")
    payload = "offerType=0&pairCurrency=1&pairRate=100000&offerAmount=1000000000000&sender=7821792282123976600" \
              "&passphrase" \
              "=11&feeATM=200000000&amountOfTime=86400&walletAddress=0x3d81757ee49fda2af1b63ee8eb7ffa67ab4ef0ee"
    response = requests.request("POST", urls3, headers=headers, data=payload)
    print(response.text)
    print("-----------------------------------------------------------------------------")
    print("--------------------------- SELL APL for ETH --------------------------------")
    payload = "offerType=1&pairCurrency=1&pairRate=100000&offerAmount=1000000000000&walletAddress" \
              "=0x3d81757ee49fda2af1b63ee8eb7ffa67ab4ef0ee&sender=7821792282123976600&passphrase=11&feeATM=200000000" \
              "&amountOfTime=86400"
    response = requests.request("POST", urls3, headers=headers, data=payload)
    print(response.text)
    transaction2 = response.json()["transaction"]
    print("-----------------------------------------------------------------------------")
    print("--------------------------- SELL APL for ETH --------------------------------")
    payload = "offerType=1&pairCurrency=1&pairRate=100000&offerAmount=1000000000000&walletAddress" \
              "=0x3d81757ee49fda2af1b63ee8eb7ffa67ab4ef0ee&sender=7821792282123976600&passphrase=11&feeATM=200000000" \
              "&amountOfTime=86400"
    response = requests.request("POST", urls3, headers=headers, data=payload)
    print(response.text)
    print("-----------------------------------------------------------------------------")
    print("--------------------------- BUY APL for PAX --------------------------------")
    payload = "offerType=0&pairCurrency=2&pairRate=1000000&offerAmount=1000000000000&walletAddress" \
              "=0x3d81757ee49fda2af1b63ee8eb7ffa67ab4ef0ee&sender=7821792282123976600&passphrase=11&feeATM=200000000" \
              "&amountOfTime=86400"
    response = requests.request("POST", urls3, headers=headers, data=payload)
    print(response.text)
    transaction3 = response.json()["transaction"]
    print("-----------------------------------------------------------------------------")
    print("--------------------------- BUY APL for PAX --------------------------------")
    payload = "offerType=0&pairCurrency=2&pairRate=1000000&offerAmount=1000000000000&walletAddress" \
              "=0x3d81757ee49fda2af1b63ee8eb7ffa67ab4ef0ee&sender=7821792282123976600&passphrase=11&feeATM=200000000" \
              "&amountOfTime=86400"
    response = requests.request("POST", urls3, headers=headers, data=payload)
    print(response.text)
    print("-----------------------------------------------------------------------------")
    print("--------------------------- SELL APL for PAX --------------------------------")
    payload = "offerType=1&pairCurrency=2&pairRate=1000000&offerAmount=1000000000000&walletAddress" \
              "=0xd17ebebd28b1b26505787c5798b339cbdb31ff77&sender=7821792282123976600&passphrase=11&feeATM=200000000" \
              "&amountOfTime=86400"
    response = requests.request("POST", urls3, headers=headers, data=payload)
    print(response.text)
    transaction4 = response.json()["transaction"]
    print("-----------------------------------------------------------------------------")
    print("--------------------------- SELL APL for PAX --------------------------------")
    payload = "offerType=1&pairCurrency=2&pairRate=1000000&offerAmount=1000000000000&walletAddress" \
              "=0xd17ebebd28b1b26505787c5798b339cbdb31ff77&sender=7821792282123976600&passphrase=11&feeATM=200000000" \
              "&amountOfTime=86400"
    response = requests.request("POST", urls3, headers=headers, data=payload)
    print(response.text)
    print("-----------------------------------------------------------------------------")

    print("--------------------------- Cancel <-- BUY APL for ETH --> --------------------------------")
    payload = "orderId=" + str(transaction1) + "&sender=7821792282123976600&" \
                                               "passphrase=11&" \
                                               "feeATM=100000000"
    response = requests.request("POST", urls3 + "/cancel", headers=headers, data=payload)
    print(response.text)
    print("-----------------------------------------------------------------------------")
    print("--------------------------- Cancel <-- SELL APL for ETH --> --------------------------------")
    payload = "orderId=" + str(transaction2) + "&sender=7821792282123976600&" \
                                               "passphrase=11&" \
                                               "feeATM=100000000"
    response = requests.request("POST", urls3 + "/cancel", headers=headers, data=payload)
    print(response.text)
    print("-----------------------------------------------------------------------------")
    print("--------------------------- Cancel <-- BUY APL for PAX --> --------------------------------")
    payload = "orderId=" + str(transaction3) + "&sender=7821792282123976600&" \
                                               "passphrase=11&" \
                                               "feeATM=100000000"
    response = requests.request("POST", urls3 + "/cancel", headers=headers, data=payload)
    print(response.text)
    print("-----------------------------------------------------------------------------")
    print("--------------------------- Cancel <-- SELL APL for PAX --> --------------------------------")
    payload = "orderId=" + str(transaction4) + "&sender=7821792282123976600&" \
                                               "passphrase=11&" \
                                               "feeATM=100000000"
    response = requests.request("POST", urls3 + "/cancel", headers=headers, data=payload)
    print(response.text)
    print("-----------------------------------------------------------------------------")


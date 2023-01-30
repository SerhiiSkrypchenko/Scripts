import requests
import random
import testNet1
import testNet2
import testNet3
import functions
import time

secretPhrase = "productforsell"
account = "APL-43MF-3V8U-82Y5-8Y6LW"
sender = "7946775328911853165"

secretPhraseBuy = "productforbuy"
account = "APL-B9VF-3749-NV4K-5XQSM"
buyer = "4171139236771438445"

def listProduct(url):
        listProduct = { "messageFile": "-1",
                            "requestType": "dgsListing",
                            "tags": "sell",
                            "priceATM": "1000000000", "quantity": "10",
                            "description": "product for selling from APL-43MF-3V8U-82Y5-8Y6LW",
                            "secretPhrase": secretPhrase,
                            "name": "Product For Selling "
                                + str(random.randint(1, 100)),
                            "feeATM": "3000000000",
                            "deadline": "1440",
                            "messageIsText": False,
                            "messageIsPrunable": True,
                            "sender": sender}
        response = requests.request("POST", random.choice(url) + "/apl", params=listProduct)
        print(response.json())
        time.sleep(60)




listProduct(testNet2.t2)


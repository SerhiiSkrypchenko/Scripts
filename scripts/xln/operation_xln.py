import requests
import data
import config_Luna_Wallet
import random

url = random.choice(config_Luna_Wallet.xln_mn)
headers = {
  'Content-Type': 'application/json'
}
while True:
    payload="{\r\n\"type\": -1,\r\n\"accounts\": [\r\n\"0x26639474de9966e6\"\r\n],\r\n\"accountFilterCriteria\": \"ALL\",\r\n\"first\": null,\r\n\"last\": null,\r\n\"page\": 0,\r\n\"perPage\": 1000000,\r\n\"orderBy\": \"asc\"\r\n}"
    response = requests.request("POST", url + "/api/rest/operation", headers=headers,
                                data=payload, verify=False)

    print(response.json())
    print()



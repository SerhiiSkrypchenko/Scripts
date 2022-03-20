import requests
import urllib3
urllib3.disable_warnings()


def restShards(url):
    getBlockChainStatus = {"": "%2Fapl", "requestType": "getBlockchainStatus"}
    try:
        response = requests.request("GET", url + "/apl", params=getBlockChainStatus, verify=False)

        if "HTTPSConnectionPool" in response.text:
            print("ERROR HTTPSConnectionPool")
        else:

            version = response.json()["version"]
            print("BACK END VERSION on " + url + " = " + version)

    except Exception as ex:
        print("Error: " + str(ex))
    except requests.HTTPError as http_err:
        print(f'HTTP err occured: {http_err}')

    try:
        response = requests.request("GET", url + "/rest/shards", verify=False)
        if "HTTPSConnectionPool" in response.text:
            print("ERROR HTTPSConnectionPool")
        else:
            print(response.text)
    except requests.HTTPError as http_err:
        print(f'HTTP err occured: {http_err}')
    except Exception as err:
        print(f'other error: {err}')

    querystring = {"": "%2Fapl", "requestType": "getBlock"}
    response = requests.request("GET", url + "/apl", params=querystring, verify=False)
    if response:
        currentHeight = response.json()["height"]
        print("Current Height on " + url + " = " + str(currentHeight) + " blocks ")
    currentHeight = 0
    print("------------ END -----------")
    print("                            ")


print("APOLLO WALLET")
print("<<<<< node0, Ohio -  52.14.238.150 >>>>>>")
restShards("https://3.141.234.52:443")

print("<<<<< node-v ,Virginia -  52.1.49.185 >>>>>>")
restShards("https://52.1.49.185:443")
print("<<<<< node1, Ohio -  13.58.228.195 >>>>>>")
restShards("https://18.188.151.122:443")
print("<<<<< node2 , Ohio -  18.191.177.177 >>>>>>")
restShards("https://3.19.83.112:443")











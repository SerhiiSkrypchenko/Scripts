import requests

xln_t2_1 = "http://163.172.130.129"
xln_t2_2 = "http://163.172.191.246"
xln_t2_3 = "http://163.172.168.167"

xln_t2 = ([xln_t2_1])

#tn2 = 12345
#tn3 = 1

def stopForgingTn(url):
    print("----------------------------------------------------------------------")
    querystring = {"requestType": "stopForging", "adminPassword": "0"}
    response = requests.request("POST", url + "/xln-api", params=querystring)
    print(response.text)
    print(" <<< ------------------  FORGING STOPPED ON " + url + " ---------------------- >>> ")

stopForgingTn(xln_t2_1)
#stopForgingTn(xln_t2_2)
#stopForgingTn(xln_t2_3)







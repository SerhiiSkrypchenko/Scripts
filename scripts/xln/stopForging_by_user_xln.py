import requests


xln_t2_1 = "http://163.172.130.129"
xln_t2_2 = "http://163.172.191.246"
xln_t2_3 = "http://163.172.168.167"

xln_t2 = ([xln_t2_1])

#tn2 = 12345
#tn3 = 1

def stopForgingByAccount(url):
    print("----------------------------------------------------------------------")
    querystring = {"requestType": "stopForging", "secretPhrase": "LunaInitAccount"}
    response = requests.request("POST", url + "/xln-api", params=querystring)
    print(response.json())
    print(" <<< ------------------  FORGING STOPPED ON  " + url + "     ---------------------- >>> ")

stopForgingByAccount(xln_t2_1)
stopForgingByAccount(xln_t2_2)
stopForgingByAccount(xln_t2_3)








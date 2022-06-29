import requests
import data

port = ":9090"

"""xln_t2_1 = "http://51.15.140.181" + port
xln_t2_2 = "http://163.172.157.196" + port
xln_t2_3 = "http://163.172.177.38" + port
xln_t2_4 = "http://51.15.228.5" + port
xln_t2_5 = "http://212.47.226.145" + port
xln_t2_6 = "http://51.15.218.18" + port"""

"""xln_t2_1 = "http://st0.dfs.t2.testnet.lunaonewallet.com"
xln_t2_2 = "http://st1.dfs.t2.testnet.lunaonewallet.com"
xln_t2_3 = "http://st2.dfs.t2.testnet.lunaonewallet.com"
xln_t2_4 = "http://st3.dfs.t2.testnet.lunaonewallet.com"
xln_t2_5 = "http://st4.dfs.t2.testnet.lunaonewallet.com"
xln_t2_6 = "http://st6.dfs.t2.testnet.lunaonewallet.com"""

xln_t2_1 = "https://store0.dfs-tn1.firstbridge.work"
xln_t2_2 = "https://store1.dfs-tn1.firstbridge.work"
xln_t2_3 = "https://store2.dfs-tn1.firstbridge.work"
xln_t2_4 = "https://store3.dfs-tn1.firstbridge.work"
xln_t2_5 = "https://store4.dfs-tn1.firstbridge.work"
#xln_t2_6 = "https://store5.dfs-tn1.firstbridge.work"




#xln_t2 = ([xln_t2_1])
xln_t2 = ([xln_t2_3, xln_t2_2, xln_t2_1, xln_t2_4, xln_t2_5])

tn2_Admin_Password = "12345"
tn3_Admin_Password = "1"

pass_admin = tn2_Admin_Password


response = requests.request("GET", xln_t2_1 + "/q/health", headers=data.headers)
print(response.json())



response = requests.request("GET", xln_t2_2 + "/q/health", headers=data.headers)
print(response.json())


response = requests.request("GET", xln_t2_3 + "/q/health", headers=data.headers)
print(response.json())


response = requests.request("GET", xln_t2_4 + "/q/health", headers=data.headers)
print(response.json())


response = requests.request("GET", xln_t2_5 + "/q/health", headers=data.headers)
print(response.json())

#response = requests.request("GET", xln_t2_6 + "/q/health", headers=data.headers)
#print(response.json())



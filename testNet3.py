import random

# Testnet 3
url1 = "http://51.15.250.32/apl"
url2 = "http://51.15.253.171/apl"
url3 = "http://51.15.210.116/apl"
url4 = "http://51.15.242.197/apl"
url5 = "http://51.15.218.241/apl"

peer1 = "apl-t3-1.testnet3.apollowallet.org"
peer2 = "apl-t3-2.testnet3.apollowallet.org"
peer3 = "apl-t3-3.testnet3.apollowallet.org"
peer4 = "apl-t3-4.testnet3.apollowallet.org"
peer5 = "apl-t3-5.testnet3.apollowallet.org"
peer6 = "wallet.testnet3.apollowallet.org"
#peer1 = "51.15.250.32"
#peer2 = "51.15.253.171"
#peer3 = "51.15.210.116"
#peer4 = "51.15.242.197"
#peer5 = "51.15.218.241"
#peer6 = "51.15.130.37"
#peer7 = "51.15.46.49"  #mixer
#peer8 = "51.15.102.159" #delphi
localhost = "localhost:7876"
local = ([localhost])
exchange_peers = ([peer2])
#t3 = ([peer1, peer2])
#t3 = ([localhost])

t3 = ([peer2, peer3, peer4, peer5, peer1, peer6])
#t3 = ([peer1, peer3])
mixer = ([peer1])
#t3_apl = (["apl-t3-1.testnet3.apollowallet.org", "apl-t3-2.testnet3.apollowallet.org", "apl-t3-3.testnet3.apollowallet.org", "apl-t3-4.testnet3.apollowallet.org", "apl-t3-5.testnet3.apollowallet.org"])
#t3 = ([peer1, peer2, peer3, peer4, peer6])
t3_apl = (["apl-t3-1.testnet3.apollowallet.org"])

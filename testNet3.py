import random

# Testnet 3
url1 = "http://51.15.250.32/apl"
url2 = "http://51.15.253.171/apl"
url3 = "http://51.15.210.116/apl"
url4 = "http://51.15.242.197/apl"
url5 = "http://51.15.218.241/apl"
port = ":7876"
peer1 = "https://apl-t3-1.testnet3.apollowallet.org"
peer2 = "https://apl-t3-2.testnet3.apollowallet.org"
peer3 = "https://apl-t3-3.testnet3.apollowallet.org"
peer4 = "https://apl-t3-4.testnet3.apollowallet.org"
peer5 = "https://apl-t3-5.testnet3.apollowallet.org"
peer6 = "https://wallet.testnet3.apollowallet.org"
peer7 = "https://apl-t3-delphi.testnet3.apollowallet.org"


"""peer1 = "http://51.15.250.32" + port
peer2 = "http://51.15.253.171" + port
peer3 = "http://51.15.210.116" + port
#peer3 = "51.15.210.116"
peer4 = "http://51.15.242.197" + port
peer5 = "http://51.15.218.241" + port
peer6 = "http://51.15.130.37" + port
peer7 = "51.15.46.49" + port  #mixer
peer8 = "http://51.15.102.159" + port #delphi"""
localhost = "localhost:7876"
local = ([localhost])
exchange_peers = ([peer2])
#t3 = ([peer1, peer2])
#t3 = ([localhost])

t3 = ([peer1, peer3, peer4, peer5, peer6])
#t3 = ([peer1, peer3])
mixer = ([peer2, peer1, peer3])
#t3_apl = (["apl-t3-1.testnet3.apollowallet.org", "apl-t3-2.testnet3.apollowallet.org", "apl-t3-3.testnet3.apollowallet.org", "apl-t3-4.testnet3.apollowallet.org", "apl-t3-5.testnet3.apollowallet.org"])
#t3 = ([peer1, peer2, peer3, peer4, peer6])
t3_apl = (["apl-t3-1.testnet3.apollowallet.org"])

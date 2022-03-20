import random
import requests
from tkinter import messagebox

# Test Net 2
localhost = "localhost:7876"
#peer1 = "51.15.37.165"
#peer4 = "51.15.209.252"
#peer5 = "51.15.228.90"
#peer2 = "51.15.228.126"
#peer3 = "51.15.228.171"
#peer6 = "51.15.46.25"
#peer7 = "51.15.72.23

peer1 = "https://apl-t2-1.testnet2.apollowallet.org"
peer2 = "https://apl-t2-2.testnet2.apollowallet.org"
peer3 = "https://apl-t2-3.testnet2.apollowallet.org"
peer4 = "https://apl-t2-4.testnet2.apollowallet.org"
peer5 = "https://apl-t2-5.testnet2.apollowallet.org"
peer6 = "https://apl-redesign.testnet2.apollowallet.org"
peer7 = "https://apl-exchange.testnet.apollowallet.org"

"""peer4 = "51.15.209.252"
peer5 = "51.15.228.90"
peer2 = "51.15.228.126"
peer3 = "51.15.228.171"
peer6 = "51.15.46.25"
peer7 = "51.15.72.23"""
localhost = "http://localhost:7876"
ropsten = "ropsten0.dex.apollowallet.org"
ropsten1 = "ropsten1.dex.apollowallet.org"
#peer8 = "51.15.100.44"
#peer9 = "51.15.233.93"
t2All = ([peer4, peer2, peer5, peer6, peer3])
#t2All = ([localhost])
#t2 = ([peer6])
t2 = ([peer2, peer3, peer4])
p1 = ([peer2, peer3])

local = ([localhost])
exchange_peers = ([peer1])
peerPoll = (["51.15.228.126"])
mixer = (["apl-t2-2.testnet2.apollowallet.org"])

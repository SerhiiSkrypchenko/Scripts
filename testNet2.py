import random
import requests
from tkinter import messagebox

# Test Net 2
localhost = "localhost:7876"
peer1 = "51.15.37.165"
#peer1 = "apl-t2-1.testnet2.apollowallet.org"
peer2 = "51.15.209.252"
peer3 = "51.15.228.90"
peer4 = "51.15.228.126"
peer5 = "51.15.228.171"
peer6 = "51.15.46.25"
peer7 = "51.15.72.23"
localhost = "localhost:7876"
#peer8 = "51.15.100.44"
#peer9 = "51.15.233.93"
t2All = ([peer2, peer3, peer4, peer6, peer1, peer5, peer7])

<<<<<<< Updated upstream
t2 = ([peer2, peer4, peer5, peer6, peer3, peer7])
=======
t2 = ([peer5, peer7, peer6, peer1, peer3])
#t2 = ([peer2, peer6, peer4, peer7, peer3])
>>>>>>> Stashed changes
local = ([localhost])
exchange_peers = ([peer1])
peerPoll = (["51.15.228.126"])

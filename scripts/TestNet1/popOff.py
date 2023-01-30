import requests

import random
import functions
import testNet1
import testNet2
import testNet3
import karantin


#functions.popOffByHeight(testNet3.peer1, 1000)
#functions.popOffByHeight("51.15.210.116", 89000)
#functions.popOffByHeight("51.15.242.197", 89000)
#functions.popOffByHeight("51.15.218.241", 89000)

#functions.popOffByBlocks(testNet2.peer1, 2000)
functions.popOffByBlocks(testNet2.peer2, 100)
functions.popOffByBlocks(testNet2.peer3, 100)
functions.popOffByBlocks(testNet2.peer4, 100)
functions.popOffByBlocks(testNet2.peer5, 100)
#functions.popOffByBlocks(testNet3.peer5, 100)
#functions.popOffByBlocks(testNet2.peer5, 20)
#functions.popOffByBlocks(karantin.peer1, 4000)
#functions.popOffByBlocks(karantin.peer4, 4000)
#functions.popOffByBlocks(testNet2.peer5, 3100)
"""functions.popOffByBlocks(testNet1.peer2, 30)
functions.popOffByBlocks(testNet1.peer3, 30)
functions.popOffByBlocks(testNet1.peer4, 30)
functions.popOffByBlocks(testNet1.peer5, 30)
functions.popOffByBlocks(testNet1.peer6, 30)
functions.popOffByBlocks(testNet1.peer7, 30)"""
#functions.popOffByBlocks("51.15.102.241", 15000)

#functions.popOffByBlocks("https://apl-tap-3.testnet-ap.apollowallet.org", 30)



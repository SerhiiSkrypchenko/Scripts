import exchangeFunctions
import requests
import random
import functions
from testNet1 import t1
from testNet1 import localhost
import mainNet
from testNet2 import t2
import testNet3
import testNet2
from exchangeFunctions import dexBuySellETH

#exchangeFunctions.exchangeTransactions(testNet3.local, 0, 1)

dexBuySellETH(testNet2.exchange_peers, 1, 3)
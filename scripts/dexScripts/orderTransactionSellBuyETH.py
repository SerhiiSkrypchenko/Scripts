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

#exchangeFunctions.exchangeTransactions(testNet3.localhost, 0, 1)

exchangeFunctions.exchangeTransactionsOneByOneSellBuy(testNet3.localhost, 1, 40)

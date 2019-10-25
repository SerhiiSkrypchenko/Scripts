import requests
import random
import string
from testNet2 import *
from testNet1 import *
from testNet3 import *
import testNet1
import testNet2
import testNet3
from functions import shufflingTransactions

#
#shufflingTransactions(30, testNet3.t3)
#shufflingTransactions(30, testNet1.t1)
shufflingTransactions(30, testNet2.t2All)

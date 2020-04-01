import requests
import random
import functions
from testNet1 import t1
from testNet1 import localhost
import mainNet
from testNet2 import t2
import testNet3
import testNet2
import testNet1

#functions.getBlockIdTn(677097, testNet1.t1)
#functions.getBlockId(676400, testNet1.localhost)

local = input("Enter local + or -: ")
testNet = input("Enter TestNet (t1, t2 or t3) for calling restShards function: ")
if local == "+":
    functions.restShards(localhost)
elif local == "-":
    print("local is skipped")
else:
    print("entered local is invalid")
if testNet == "t1":
    functions.restShardsTn(testNet1.t1)
elif testNet == "t3":
    functions.restShardsTn(testNet3.t3)
elif testNet == "t2":
    functions.restShardsTn(testNet2.t2)
else:
    print("entered testNet is invalid")


#functions.restShards(localhost)
#functions.restShardsTn(t1)
#functions.restShardsTn(testNet2.t2)

#functions.restShardsTn(testNet3.t3)






import functions
from testNet1 import localhost
import testNet3
import testNet2
import testNet1
import testNet4_tap
import testNetStage



local = input("Enter local + or -: ")
testNet = input("Enter TestNet (t1, t2, t3 ot stage) for calling restShards function: ")
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
elif testNet == "t4":
    functions.restShardsTn(testNet4_tap.t4)
elif testNet == "stage":
    functions.restShardsTn(testNetStage.t15All)
else:
    print("entered testNet is invalid")


#functions.restShards(localhost)
#functions.restShardsTn(t1)
#functions.restShardsTn(testNet2.t2)
#functions.restShardsTn(testNet3.t3)






from functions import sendMoneyToAccounts
from functions import sendMoneyToManyAccounts
import testNet1
import testNet2
import testNet3
import threading

wallet_count = 20000000
thread_count = 20

def thread_function(i):
    start = (int)(wallet_count/thread_count)*(i+20)
    print("----------START-------------" + str(i))
    print("START = " + (str)(start))
    end = (int)(wallet_count/thread_count)*(i+21)
    print("END = " + (str)(end))
    print("--------- END -------------" + str(i))
    sendMoneyToManyAccounts(testNet2.peer2, end, start)

for i in range(thread_count):
    x = threading.Thread(target=thread_function, args=(i,))
    x.start()





import time

#print('The time is      :', time.ctime())
#later = time.time() + 36000
#print('15 secs from now :', time.ctime(later))




print('The time is      :', time.ctime())
start = time.time()
finish = time.time() + 25
print('25 secs from now :', time.ctime(finish))
while (start < finish):
    print(" try one more time ")
    time.sleep(10)
    start = time.time()
    print('Current time is:', time.ctime(start))
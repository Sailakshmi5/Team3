from threading import *
import time
l=Lock()
def wish(name):
    l.acquire()
    for i in range(10):
        print("good eveening ",end=" ")
        time.sleep(2)
        print(name)
    l.release()
t1=Thread(target=wish,args={'jose'})
t2=Thread(target=wish,args={'mitch'})
t3=Thread(target=wish,args={'mart'})
t1.start()
#t1.join()
t2.start()
#t2.join()
t3.start()
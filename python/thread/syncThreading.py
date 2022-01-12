#!/usr/bin/python3
import threading
import time

threadLock = threading.Lock()

class MyThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print('线程开始：'+self.name)
        threadLock.acquire()
        print_time(self.name,self.delay,5)
        print('线程结束：'+self.name)
        threadLock.release()

def print_time(threadName,delay,counter):
    while counter:
        print("%s %s" % (threadName,time.ctime(time.time())))
        time.sleep(delay)
        counter -=1

# 创建两个线程
try:
    threading1 = MyThread(1,'线程1',1)
    threading2 = MyThread(2, '线程2', 2)
    # 启动线程
    threading1.start()
    threading2.start()

    threading1.join()
    threading2.join()
    print('执行完成！')
except:
    print('线程启动失败！')
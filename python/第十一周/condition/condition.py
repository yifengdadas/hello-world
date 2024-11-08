import threading
import time
import random
from collections import deque

condition=threading.Condition()
buffer=deque(maxlen=5)

def producer():
    global count
    count=0
    while True:
        count+=1
        item=random.randint(1,100)
        with condition:
            while len(buffer)==buffer.maxlen:
                condition.wait()
            buffer.append(item)
            print(f"生产了产品{item},当前缓冲区大小:{len(buffer)}")
            condition.notify()
        time.sleep(random.uniform(0.1,1))

def consumer():
    while True:
        with condition:
            condition.wait()
            item=buffer.popleft()
            print(f"消费了产品{item},当前缓冲区大小:{len(buffer)}")
            condition.notify()
            time.sleep(random.uniform(0.1,1))

producer_thread_obj=threading.Thread(target=producer)
consumer_thread_obj=threading.Thread(target=consumer)

producer_thread_obj.start()
consumer_thread_obj.start()
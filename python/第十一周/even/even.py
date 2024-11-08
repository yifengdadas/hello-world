import threading
import time
import random

event=threading.Event()

def count_thread():
    global count
    count=0
    while count<10:
        count+=1
        print(f"计数:{count}")
        time.sleep(random.uniform(0.1,1))
    event.set()

def print_thread():
    event.wait()
    print("已完成计数")

count_thread_obj=threading.Thread(target=count_thread)
print_thread_obj=threading.Thread(target=print_thread)

count_thread_obj.start()
print_thread_obj.start()

count_thread_obj.join()
print_thread_obj.join()
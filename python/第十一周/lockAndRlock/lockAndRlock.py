import threading
import time

counter=0

lock=threading.Lock()
lock_acqired_by=None

def increment_with_lock(thread_id,n):
    global counter
    for _ in range(n):
        lock.acquire()
        lock_acqired_by=threading.current_thread().name
        print(f"Thread{lock_acqired_by}acquired lock,counter:{counter}")
        counter+=1
        print(f"Thread{lock_acqired_by}incremented counter to{counter}")
        lock.release()
        lock_acqired_by=None
        time.sleep(0.001)

rlock=threading.RLock()
rlock_acquired_by=None

def increment_with_rlock(thread_id,n):
    global counter
    for _ in range(n):
        rlock.acquire()
        rlock_acquired_by=threading.current_thread().name
        print(f"Thread{rlock_acquired_by}acquired RLock,counter:{counter}")
        counter+=1
        print(f"Thread{rlock_acquired_by}incremented counter to:{counter}")
        rlock.release()
        rlock_acquired_by=None
        time.sleep(0.001)

if __name__=="__main__":
    num_threads=5
    increment_times=20

    threads_with_lock=[]
    for i in range(num_threads):
        t=threading.Thread(target=increment_with_lock,args=(i,increment_times))
        threads_with_lock.append(t)
        t.start()

    for t in threads_with_lock:
        t.join()

    for t in threads_with_lock:
        t.join()

    for t in threads_with_lock:
        t.join()

    print(f"Final counter with Lock:{counter}")

    counter=0
    threads_with_rlock=[]
    for i in range(num_threads):
        t=threading.Thread(target=increment_with_rlock,args=(i,increment_times))
        threads_with_rlock.append(t)
        t.start()

    for t in threads_with_rlock:
        t.join()

    print(f"Final counter with RLock:{counter}")
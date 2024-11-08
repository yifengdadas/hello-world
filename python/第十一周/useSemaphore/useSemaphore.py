import threading
import time
import random

N=5

semaphore=threading.Semaphore(N)

resource_pool=[f"Resource_{i}"for i in range(N)]

def access_resource(resource_name,semaphore,sleep_time):
    print(f"Thread{threading.current_thread().name}is trying to access{resource_name}")
    semaphore.acquire()
    print(f"Thread{threading.current_thread().name}has acquired{resource_name}")
    time.sleep(sleep_time)
    print(f"Thread{threading.current_thread().name}is releasing{resource_name}")
    semaphore.release()

if __name__=="__main__":
    num_threads=10
    sleep_times=[random.uniform(0.1,1.0)for _ in range (num_threads)]

    threads=[]
    for i in range(num_threads):
        resource=resource_pool[i%N]
        t=threading.Thread(target=access_resource,args=(resource,semaphore,sleep_times[i]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All threads have finished accessing resources.")
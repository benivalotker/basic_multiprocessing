import time
import queue
from multiprocessing import current_process

'''
Queue
'''
def queue_task(task_queue, number):
    while True:
        try:
            task = task_queue.get_nowait() 
        except queue.Empty:
            break
        else:
            print(current_process().name, "run " + task)
            time.sleep(5)


'''
Pool
'''
def pool_task(params):
    if params%2 == 0:
        return params
    else:
        return 0


'''
Lock (with shared counter)
    * lock - promise that counter will be 40
    * no lock - not promise that conter will be 40 (he cab be less)
'''
def lock_task(counter, lock):
    for _ in range(10):
        lock.acquire()
        try:
            counter.value += 1
            print(current_process().name, " INC - ", str(counter.value))
            time.sleep(2)
        finally:
            lock.release()

def no_lock_task(counter, lock):
    for _ in range(10):
        counter.value += 1
        print(current_process().name, " INC - ", str(counter.value))
        time.sleep(2)


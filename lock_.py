#/path/path/
#title           :Title 
#description     :Description.
#update date     :01/01/2020 12:10
#version         :1.0
#changes         :new version changes description.
#python_version  :3.6  
#==============================================================================

from multiprocessing import Process, Lock, Value
from task_function import lock_task, no_lock_task


# processes to create
processes_number = 4

# proccess list
processes = []

if __name__ == '__main__':
    # shared counter
    counter = Value('i', 0)

    # lock object
    lock = Lock()
    
    for _ in range(processes_number):
        p = Process(target=lock_task, args=(counter, lock))
        #p = Process(target=no_lock_task, args=(counter, lock))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("finish main process")
    
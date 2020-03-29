#/path/path/
#title           :Title 
#description     :Description.
#update date     :01/01/2020 12:10
#version         :1.0
#changes         :new version changes description.
#python_version  :3.6  
#==============================================================================

from task_function import queue_task
from multiprocessing import Process, Queue

def main():    
    # processes to create
    processes_number = 4

    # queue - first in first out
    task = Queue()
    
    # proccess list
    processes = []

    # add task to queue
    for i in range(10):
        task.put("task number " + str(i))

    # creating processes
    for number in range(processes_number):
        p = Process(target=queue_task, args=(task, number))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


if __name__ == '__main__':
    main()
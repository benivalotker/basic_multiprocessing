#/path/path/
#title           :Title 
#description     :Description.
#update date     :01/01/2020 12:10
#version         :1.0
#changes         :new version changes description.
#python_version  :3.6  
#==============================================================================

import multiprocessing
from task_function import pool_task

# iterable object
task_params = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def main():
    # create multiprocessing pool
    p = multiprocessing.Pool(multiprocessing.cpu_count())

    # run the task
    res = p.map(pool_task, task_params)

    p.close()
    p.join()

    # print the result
    print(res)

if __name__ == "__main__":
    main()
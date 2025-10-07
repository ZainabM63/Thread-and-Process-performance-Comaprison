from do_something import *
import time
import multiprocessing
import threading

if __name__ == "__main__":
    size = 1000  # workload size
    procs = 5      # number of processes
    jobs = []

    
    # Multiprocessing
    
    start_time = time.time()
    out_list = multiprocessing.Manager().list()

    for i in range(procs):
        process = multiprocessing.Process(target=do_something, args=(size, out_list))
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("Multiprocessing complete.")
    end_time = time.time()
    print("Multiprocessing time =", end_time - start_time)

    # Multithreading
    
    jobs = []
    threads = 5       # number of threads
    start_time = time.time()
    out_list = []

    for i in range(threads):
        thread = threading.Thread(target=do_something, args=(size, out_list))
        jobs.append(thread)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("Multithreading complete.")
    end_time = time.time()
    print("Multithreading time =", end_time - start_time)
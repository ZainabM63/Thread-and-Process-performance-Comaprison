import threading
import time
from do_something import do_something

def worker(thread_id, size, out_list, semaphore):
    print(f"Thread {thread_id} waiting for permit...")
    with semaphore:
        print(f"Thread {thread_id} started.")
        do_something(size, out_list)
        print(f"Thread {thread_id} finished.")

if __name__ == "__main__":
    out_list = []
    semaphore = threading.Semaphore(2)  # only 2 threads can work at once
    num_threads = 3
    size = 7

    threads = [threading.Thread(target=worker, args=(i, size, out_list, semaphore)) for i in range(num_threads)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("\nFinal Output List:", out_list)
    print("Length of list (Semaphore):", len(out_list))

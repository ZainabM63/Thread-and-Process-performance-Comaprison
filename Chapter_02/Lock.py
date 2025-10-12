
import threading
import time
from do_something import do_something

def worker(thread_id, size, out_list, lock):
    print(f"Thread {thread_id} started.")
    with lock:
        do_something(size, out_list)
    print(f"Thread {thread_id} finished.")

if __name__ == "__main__":
    out_list = []
    lock = threading.Lock()

    
    num_threads = 3      
    size = 7             
    threads = [
        threading.Thread(target=worker, args=(i, size, out_list, lock))
        for i in range(num_threads)
    ]

    for t in threads:
        t.start()
        time.sleep(0.5)  # small delay to see order clearly

    for t in threads:
        t.join()

    print("\nFinal Output List:", out_list)
    print("Length of list (Lock):", len(out_list))

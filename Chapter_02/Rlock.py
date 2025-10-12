
import threading
import time
from do_something import do_something

def worker(thread_id, size, out_list, rlock):
    print(f"Thread {thread_id} started.")
    with rlock:
        # re-acquire lock inside to demonstrate reentrancy
        with rlock:
            do_something(size, out_list)
    print(f"Thread {thread_id} finished.")

if __name__ == "__main__":
    out_list = []
    rlock = threading.RLock()
    num_threads = 3
    size = 7

    threads = [threading.Thread(target=worker, args=(i, size, out_list, rlock)) for i in range(num_threads)]

    for t in threads:
        t.start()
        time.sleep(0.5)
    for t in threads:
        t.join()

    print("\nFinal Output List:", out_list)
    print("Length of list (RLock):", len(out_list))

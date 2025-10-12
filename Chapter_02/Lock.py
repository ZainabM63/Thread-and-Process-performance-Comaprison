
import threading
from do_something import do_something

def worker(size, out_list, lock):
    with lock:
        do_something(size, out_list)

if __name__ == "__main__":
    out_list = []
    lock = threading.Lock()

    threads = [threading.Thread(target=worker, args=(100000, out_list, lock)) for _ in range(4)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("Length of list (Lock):", len(out_list))

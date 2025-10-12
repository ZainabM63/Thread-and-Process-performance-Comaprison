
import threading
from do_something import do_something

def worker(size, out_list, rlock):
    with rlock:
        do_something(size, out_list)

if __name__ == "__main__":
    out_list = []
    rlock = threading.RLock()

    threads = [threading.Thread(target=worker, args=(100000, out_list, rlock)) for _ in range(4)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("Length of list (RLock):", len(out_list))

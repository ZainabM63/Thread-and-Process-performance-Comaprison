
import threading
from do_something import do_something

def worker(size, out_list, semaphore):
    with semaphore:
        do_something(size, out_list)

if __name__ == "__main__":
    out_list = []
    semaphore = threading.Semaphore(2)  # limit 2 threads at once

    threads = [threading.Thread(target=worker, args=(100000, out_list, semaphore)) for _ in range(4)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("Length of list (Semaphore):", len(out_list))

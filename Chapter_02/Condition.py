
import threading
from do_something import do_something

def worker(size, out_list, condition):
    do_something(size, out_list)
    with condition:
        condition.notify()  # notify monitor after finishing

def monitor(out_list, condition, total_expected):
    with condition:
        while len(out_list) < total_expected:
            condition.wait()
            print(f"Monitor: Current length = {len(out_list)}")

if __name__ == "__main__":
    out_list = []
    condition = threading.Condition()
    num_threads = 4
    size = 100000

    threads = [threading.Thread(target=worker, args=(size, out_list, condition)) for _ in range(num_threads)]
    monitor_thread = threading.Thread(target=monitor, args=(out_list, condition, size * num_threads))

    monitor_thread.start()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    monitor_thread.join()

    print("Final length (Condition):", len(out_list))

import multiprocessing
import time
from do_something import do_something  # Import function from do_something.py

if __name__ == '__main__':
    size = 1000
    out_list1 = multiprocessing.Manager().list()
    out_list2 = multiprocessing.Manager().list()

    process_with_name = multiprocessing.Process(
        name='do_something process 1',
        target=do_something,
        args=(size, out_list1)
    )

    process_with_default_name = multiprocessing.Process(
        target=do_something,
        args=(size, out_list2)
    )

    start_time = time.time()
    process_with_name.start()
    process_with_default_name.start()

    process_with_name.join()
    process_with_default_name.join()
    end_time = time.time()

    print(f"Process 1 output list length: {len(out_list1)}")
    print(f"Process 2 output list length: {len(out_list2)}")
    print(f"Total execution time: {end_time - start_time:.2f} seconds")

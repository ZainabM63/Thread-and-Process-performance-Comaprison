import multiprocessing
import time
from do_something import do_something  # Import external function

def foo():
    name = multiprocessing.current_process().name
    print(f"Starting {name}\n")

    out_list = multiprocessing.Manager().list()

    if name == 'background_process':
        do_something(5, out_list)
    else:
        do_something(10, out_list)

    time.sleep(1)
    print(f"Exiting {name}\n")

if __name__ == '__main__':
    background_process = multiprocessing.Process(
        name='background_process',
        target=foo
    )
    background_process.daemon = True

    NO_background_process = multiprocessing.Process(
        name='NO_background_process',
        target=foo
    )
    NO_background_process.daemon = False

    background_process.start()
    NO_background_process.start()

    background_process.join(timeout=2)
    NO_background_process.join()

import multiprocessing
import time
from do_something import do_something  # <-- imported function

def foo():
    name = multiprocessing.current_process().name
    print("Starting %s \n" % name)
    if name == 'background_process':
        for i in range(0, 5):
            print('---> %d \n' % i)
        time.sleep(1)
    else:
        # Instead of running foo logic here, call imported function
        do_something()
        time.sleep(1)
    print("Exiting %s \n" % name)


if __name__ == '__main__':
    background_process = multiprocessing.Process(
        name='background_process',
        target=foo
    )
    background_process.daemon = False

    NO_background_process = multiprocessing.Process(
        name='NO_background_process',
        target=foo
    )
    NO_background_process.daemon = False

    background_process.start()
    NO_background_process.start()

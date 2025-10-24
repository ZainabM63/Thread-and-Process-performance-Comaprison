import multiprocessing
import time
from do_something import do_something 

def run_task():
    print('Starting function (replaced with do_something)')
    out_list = multiprocessing.Manager().list()
    do_something(10, out_list)
    print(f'Finished function with {len(out_list)} results.')

if __name__ == '__main__':
    p = multiprocessing.Process(target=run_task)
    print('Process before execution:', p, p.is_alive())
    p.start()
    print('Process running:', p, p.is_alive())
    time.sleep(2)
    p.terminate()
    print('Process terminated:', p, p.is_alive())
    p.join()
    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)

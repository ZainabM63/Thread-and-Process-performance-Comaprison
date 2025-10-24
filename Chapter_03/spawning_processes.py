import multiprocessing
from do_something import do_something  # Import external function

def myFunc(i):
    print(f'calling do_something from process no: {i}')
    out_list = multiprocessing.Manager().list()
    do_something(i * 1000, out_list)
    print(f'Process {i} finished with {len(out_list)} results.')

if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()

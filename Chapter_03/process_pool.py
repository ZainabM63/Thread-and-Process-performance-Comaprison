import multiprocessing
from do_something import do_something  # imported function

def function_square(data):
    do_something()  
    result = data * data
    return result


if __name__ == '__main__':
    inputs = list(range(0, 10))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_square, inputs)

    pool.close()
    pool.join()
    print('Pool:', pool_outputs)

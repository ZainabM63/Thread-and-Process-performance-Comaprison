import multiprocessing
from do_something import do_something

def function_square(data):
    results = []
    do_something(2, results)     # ✅ correct call
    result = data * data
    return result

if __name__ == '__main__':
    inputs = list(range(0, 10))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_square, inputs)

    pool.close()
    pool.join()
    print('Pool:', pool_outputs)

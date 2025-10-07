Multiprocessing vs Multithreading in Python

This project compares the performance of multiprocessing and multithreading in Python by running the same function (do_something) under different conditions. The aim is to analyze which approach performs better for the given workload and why.This function performs repeated mathematical operations (sqrt and power) and appends the results to a shared list.

Experiment Setup

Language: Python 3

Libraries Used: multiprocessing, threading, time

Workload Size: 1000 iterations

Environment: Windows 10

We tested three cases:

5 Processes vs 5 Threads

10 Processes vs 10 Threads

50 Processes vs 50 Threads

Results Case Multiprocessing Time Multithreading Time 5 Processes / 5 Threads 1.428 sec 0.044 sec 10 Processes / 10 Threads 2.438 sec 0.041 sec 50 Processes / 50 Threads 8.716 sec 0.099 sec Analysis

Multithreading consistently performed much faster than multiprocessing for workload size = 1000.

This is because the function do_something was I/O-bound (involving simulated delays such as time.sleep).

For I/O-bound tasks:

Threads are more efficient because while one thread is waiting, others can continue execution.

Python’s Global Interpreter Lock (GIL) does not significantly affect performance in such cases.

For multiprocessing:

Each process has its own memory space and requires additional overhead.

Context switching, inter-process communication, and resource allocation introduce delays.

With a small workload (size = 1000), the overhead outweighs the benefits of parallel execution.

Conclusion

For I/O-bound tasks (such as file operations, network requests, or waiting operations), multithreading is faster and more resource-efficient.

For CPU-bound tasks (such as heavy mathematical computations, data processing, or image rendering), multiprocessing is generally more effective because it can utilize multiple CPU cores and bypass Python’s GIL.

In this experiment (size = 1000, I/O-bound workload), multithreading clearly outperforms multiprocessing.

How to Run

Clone this repository:

git clone

Run the script:

python Process_thread.py

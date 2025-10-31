
This chapter demonstrates how Python’s **`multiprocessing`** module works by creating, naming, synchronizing, managing, and terminating multiple processes.

All examples use a **CPU-bound function `do_something()`** imported from `do_something.py`, which simulates computational work.

---

## ⚙️ 1. naming_processes.py

### **Purpose**
Demonstrates how to create and name processes explicitly and observe their execution and timing.

### **Key Code**
```python
process_with_name = multiprocessing.Process(
    name='do_something process 1',
    target=do_something,
    args=(1000, out_list1)
)
process_with_default_name = multiprocessing.Process(
    target=do_something,
    args=(1000, out_list2)
)
````

### **Sample Output**

```
Process 1 output list length: 1000
Process 2 output list length: 1000
Total execution time: 0.43 seconds
```

### **Observation**

Both processes successfully executed the imported `do_something()` function concurrently.
Execution time was significantly reduced compared to running sequentially.

---

## ⚙️ 2. spawning_processes.py

### **Purpose**

To demonstrate how multiple processes can be spawned dynamically using a loop.

### **Key Code**

```python
for i in range(6):
    process = multiprocessing.Process(target=myFunc, args=(i,))
    process.start()
    process.join()
```

### **Sample Output**

```
calling do_something from process no: 0
Process 0 finished with 0 results.
calling do_something from process no: 1
Process 1 finished with 1000 results.
calling do_something from process no: 2
Process 2 finished with 2000 results.
calling do_something from process no: 3
Process 3 finished with 3000 results.
calling do_something from process no: 4
Process 4 finished with 4000 results.
calling do_something from process no: 5
Process 5 finished with 5000 results.
```

### **Observation**

Six processes were created sequentially.
Each process executed independently with different workloads (`i * 1000`).
The number of results scaled linearly with `i`, confirming correct multiprocessing behavior.

---

## ⚙️ 3. killing_processes.py

### **Purpose**

To show how to start, terminate, and join a process, and observe its lifecycle.

### **Key Code**

```python
p.start()
print('Process running:', p.is_alive())
p.terminate()
print('Process terminated:', p.is_alive())
p.join()
print('Process joined:', p.is_alive())
```

### **Sample Output**

```
Process before execution: <Process name='Process-1' ...> False
Process running: <Process name='Process-1' pid=9368 ...> True
Starting function (replaced with do_something)
Finished function with 10 results.
Process terminated: ... False
Process joined: ... False
Process exit code: 0
```

### **Observation**

The process was started, executed, and terminated cleanly.
Exit code `0` confirms successful execution.
Demonstrates safe use of `.start()`, `.terminate()`, and `.join()` methods.

---

## ⚙️ 4. run_background_processes_no_daemons.py

### **Purpose**

To demonstrate daemon vs non-daemon processes and verify behavior when using an imported computational function.

### **Key Code**

```python
background_process.daemon = True
NO_background_process.daemon = False
```

### **Sample Output**

```
Starting background_process
---> 0
---> 1
---> 2
---> 3
---> 4
Starting NO_background_process
Results from do_something(): [0.0, 1.0, 2.0000000000000004]
Exiting background_process
Exiting NO_background_process
```

### **Observation**

The non-daemon process executed successfully and returned results from `do_something()`.
Daemon processes terminated automatically when the main program exited, demonstrating that background (daemon) processes are dependent on the main process lifecycle.

---

## ⚙️ 5. processes_barrier.py

### **Purpose**

To demonstrate synchronization of multiple processes using `Barrier` and `Lock`.

### **Key Code**

```python
synchronizer = Barrier(2)
serializer = Lock()
Process(name='p1 - test_with_barrier',
        target=test_with_barrier,
        args=(synchronizer, serializer)).start()
```

### **Sample Output**

```
process p3 - test_without_barrier ----> 2025-11-01 00:27:31.337429
p3 - test_without_barrier results: [0.0, 1.0]
process p4 - test_without_barrier ----> 2025-11-01 00:27:31.356129
p4 - test_without_barrier results: [0.0, 1.0]
process p2 - test_with_barrier ----> 2025-11-01 00:27:31.361577
p2 - test_with_barrier results: [0.0, 1.0]
process p1 - test_with_barrier ----> 2025-11-01 00:27:31.361577
p1 - test_with_barrier results: [0.0, 1.0]
```

### **Observation**

Processes with the barrier waited until all participants reached the synchronization point.
The results from `do_something()` were printed in an orderly manner due to proper synchronization and locking.

---

## ⚙️ 6. process_pool.py

### **Purpose**

To demonstrate parallel processing using a `multiprocessing.Pool`.

### **Key Code**

```python
inputs = list(range(0,10))
pool = multiprocessing.Pool(processes=4)
pool_outputs = pool.map(do_something, inputs)
```

### **Sample Output**

```
Pool: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### **Observation**

The pool efficiently distributed work across 4 processes.
Each input was processed by `do_something()`, producing squared results concurrently.

---

## 🧮 Summary Table

| Script                                 | Purpose                               | Success | Key Observation                                         |
| :------------------------------------- | :------------------------------------ | :-----: | :------------------------------------------------------ |
| naming_processes.py                    | Process naming and parallel execution |    ✅    | Both processes ran concurrently with shorter total time |
| spawning_processes.py                  | Spawn multiple processes in loop      |    ✅    | Independent execution, scalable workload                |
| killing_processes.py                   | Start, terminate, and join process    |    ✅    | Proper lifecycle control verified                       |
| run_background_processes_no_daemons.py | Daemon vs Non-Daemon behavior         |    ✅    | Daemon terminated early; non-daemon completed normally  |
| processes_barrier.py                   | Synchronization with Barrier & Lock   |    ✅    | Ordered execution achieved using synchronization        |
| process_pool.py                        | Parallel execution using Pool         |    ✅    | Parallel results computed efficiently                   |

---

## 🧩 Conclusion

Through these experiments, the following key insights were observed:

* Multiprocessing enables **true parallelism** for CPU-bound tasks, improving performance.
* **Naming and synchronization** help manage and debug concurrent processes.
* **Lifecycle management** (`start()`, `terminate()`, `join()`) ensures process control and safety.
* **Daemon processes** terminate with the main process, while non-daemon processes continue independently.
* **Process pools** and **barriers** provide structured ways to manage and coordinate concurrent workloads.

---

## 🧠 Overall Learning

Python’s `multiprocessing` module provides powerful and flexible ways to achieve parallel computation.
Understanding process behavior—naming, daemonization, synchronization, and pooling—is essential for designing efficient and robust concurrent applications.

---

```

---

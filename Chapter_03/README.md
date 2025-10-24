📘 Overview

This chapter demonstrates how Python’s multiprocessing module works by creating, naming, managing, and terminating multiple processes.
All examples use a CPU-bound function do_something() imported from do_something.py, which simulates computational work.

⚙️ 1. naming_processes.py
Purpose

To demonstrate how to create and name processes explicitly and observe their execution and timing.

Key Code
process_with_name = multiprocessing.Process(
    name='do_something process 1',
    target=do_something,
    args=(1000, out_list1)
)
process_with_default_name = multiprocessing.Process(
    target=do_something,
    args=(1000, out_list2)
)

Sample Output
Process 1 output list length: 1000
Process 2 output list length: 1000
Total execution time: 0.43 seconds

Observation

Both processes successfully executed the imported do_something() function concurrently.

Execution time was significantly reduced compared to running sequentially.

⚙️ 2. spawning_processes.py
Purpose

To demonstrate how multiple processes can be spawned dynamically using a loop.

Key Code
for i in range(6):
    process = multiprocessing.Process(target=myFunc, args=(i,))
    process.start()
    process.join()

Sample Output
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

Observation

Six processes were created sequentially.

Each process executed independently with different workloads (i * 1000).

The number of results scaled linearly with i, confirming correct multiprocessing behavior.

⚙️ 3. killing_processes.py
Purpose

To show how to start, terminate, and join a process, and observe its lifecycle.

Key Code
p.start()
print('Process running:', p.is_alive())
p.terminate()
print('Process terminated:', p.is_alive())
p.join()
print('Process joined:', p.is_alive())

Sample Output
Process before execution: <Process name='Process-1' ...> False
Process running: <Process name='Process-1' pid=9368 ...> True
Starting function (replaced with do_something)
Finished function with 10 results.
Process terminated: ... False
Process joined: ... False
Process exit code: 0

Observation

Process was started, executed, and terminated cleanly.

Exit code 0 confirms successful execution.

Demonstrates safe use of .start(), .terminate(), and .join() methods.

⚙️ 4. run_background_processes.py
Purpose

To demonstrate daemon vs non-daemon processes in Python.

Key Code
background_process.daemon = True
NO_background_process.daemon = False

Sample Output
Starting background_process
Starting NO_background_process
Process background_process:
AssertionError: daemonic processes are not allowed to have children
Exiting NO_background_process

Observation

The daemon process raised an error because daemon processes cannot create child processes (like the Manager() used inside do_something()).

The non-daemon process executed successfully and exited normally.

🧮 Summary Table
Script	Purpose	Success	Key Observation
naming_processes.py	Process naming and parallel execution	✅	Both processes ran concurrently with shorter total time
spawning_processes.py	Spawn multiple processes in loop	✅	Independent execution, scalable workload
killing_processes.py	Start, terminate, and join process	✅	Proper lifecycle control verified
run_background_processes.py	Daemon vs Non-Daemon behavior	⚠️ (Expected Error)	Daemon processes cannot spawn children
🧩 Conclusion

Through these experiments, the following key insights were observed:

Multiprocessing enables true parallelism for CPU-bound tasks, improving performance.

Process naming helps in debugging and identifying concurrent executions.

Lifecycle management (start(), terminate(), join()) provides full control over process execution.

Daemon processes are background workers that terminate with the main process and cannot create new child processes.

Using Managers or shared memory inside daemonic processes leads to expected errors, confirming Python’s process safety rules.

🧠 Overall Learning

Multiprocessing in Python provides efficient ways to perform parallel CPU-heavy computations.
Understanding process properties such as daemonization, naming, and synchronization is essential for designing robust concurrent programs.
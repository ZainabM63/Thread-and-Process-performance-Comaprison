# Thread Synchronization Examples in Python
### (Lock, RLock, Semaphore, and Condition)

This project demonstrates how different thread synchronization mechanisms in Python (`threading` module) control concurrent access to shared resources using a common computational function `do_something.py`.

---

## Synchronization Mechanisms Tested

### 1. Lock
**Purpose:** Ensures that only one thread modifies the shared resource (`out_list`) at a time.

**Behavior Observed:**
Thread 0 started.
Thread 0 finished.
Thread 1 started.
Thread 1 finished.
Thread 2 started.
Thread 2 finished.
Length of list (Lock): 21


**Result:** Safe access to the shared list; total length = 21 (expected).

---

### 2. RLock (Reentrant Lock)
**Purpose:** Allows the same thread to acquire the lock multiple times safely.

**Behavior Observed:**  
Similar to Lock — sequential thread completion and consistent results.

**Result:** Safe and consistent access; total length = 21.

---

### 3. Semaphore
**Purpose:** Controls access to a resource by limiting the number of threads allowed to run concurrently.

**Behavior Observed:**
Thread 0 waiting for permit...
Thread 0 started.
Thread 1 waiting for permit...
Thread 2 waiting for permit...
Thread 1 started.
Thread 0 finished.
Thread 1 finished.
Thread 2 started.
Thread 2 finished.
Length of list (Semaphore): 21


**Result:** Threads run in controlled batches; list remains consistent.

---

### 4. Condition
**Purpose:** Enables threads to wait for a certain condition to be met before proceeding.

**Behavior Observed:**
Thread 0 notifying condition.
Thread 1 notifying condition.
Thread 2 notifying condition.
Monitor: Current length = 7
Monitor: Current length = 14
Monitor: Current length = 21


**Result:** All threads signal the condition, and the monitor accurately tracks progress.

---

## Comparative Evaluation (Markdown table)
| Synchronization Type | Main Use                                  | Behavior                      | Safety | Best For                         |
|----------------------|-------------------------------------------|-------------------------------|--------|----------------------------------|
| Lock                 | Prevents simultaneous access              | Sequential execution          | Safe   | General thread safety            |
| RLock                | Reentrant version of Lock                 | Similar to Lock               | Safe   | Nested locking scenarios         |
| Semaphore            | Limits concurrent access                  | Controlled parallelism        | Safe   | Managing limited resources       |
| Condition            | Waits for specific conditions/signals     | Event-driven coordination     | Safe   | Producer-consumer models         |

---

<table>
  <thead>
    <tr>
      <th>Synchronization Type</th>
      <th>Main Use</th>
      <th>Behavior</th>
      <th>Safety</th>
      <th>Best For</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lock</td>
      <td>Prevents simultaneous access</td>
      <td>Sequential execution</td>
      <td>Safe</td>
      <td>General thread safety</td>
    </tr>
    <tr>
      <td>RLock</td>
      <td>Reentrant version of Lock</td>
      <td>Similar to Lock</td>
      <td>Safe</td>
      <td>Nested locking scenarios</td>
    </tr>
    <tr>
      <td>Semaphore</td>
      <td>Limits concurrent access</td>
      <td>Controlled parallelism</td>
      <td>Safe</td>
      <td>Managing limited resources</td>
    </tr>
    <tr>
      <td>Condition</td>
      <td>Waits for specific conditions/signals</td>
      <td>Event-driven coordination</td>
      <td>Safe</td>
      <td>Producer-consumer models</td>
    </tr>
  </tbody>
</table>

---

## Unified Conclusion

All four synchronization mechanisms — Lock, RLock, Semaphore, and Condition — successfully maintained data integrity during concurrent execution. Each method produced the expected number of items in the shared list (21) and prevented race conditions. Lock and RLock provide straightforward mutual exclusion (RLock is for reentrant/nested locking), Semaphore controls the number of simultaneous workers for limited resources, and Condition allows threads to coordinate by waiting and notifying based on state. Choose the primitive that matches your concurrency requirement: use Lock/RLock for simple mutual exclusion, Semaphore for limiting concurrent access, and Condition for coordination-driven scenarios.



## How to Run

Execute each file separately to observe the synchronization behavior:
```bash
python Chapter_02/Lock.py
python Chapter_02/RLock.py
python Chapter_02/Semaphore.py
python Chapter_02/Condition.py
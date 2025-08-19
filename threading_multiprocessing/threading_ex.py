import threading
import time


def task(name):
    print(f"{name} started")
    time.sleep(23)  # Simulate I/O (e.g. waiting for network)
    print(f"{name} finished")


# Create two threads
t1 = threading.Thread(target=task, args=("Thread-1",))
t2 = threading.Thread(target=task, args=("Thread-2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Threading example done.")

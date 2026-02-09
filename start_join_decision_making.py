import threading
import time

results = []

def work(n):
    time.sleep(2)
    results.append(n)
    print(f"Thread finished: {n}")

print("Main started")

threads = []
for i in range(5):
    t = threading.Thread(target=work, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Main thread decision point")
print("Results:", results)

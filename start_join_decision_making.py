import threading
import time

results = []

def process_task(task_id):
    time.sleep(2)
    results.append(task_id)
    print(f"Thread finished: {task_id}")

def main():
    print("Main started")

    threads = []

    for task_id in range(5):
        thread = threading.Thread(target=process_task, args=(task_id,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Main thread decision point")
    print("Results:", results)

if __name__ == "__main__":
    main()

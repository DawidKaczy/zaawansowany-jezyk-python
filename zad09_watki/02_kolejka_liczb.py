import threading
import queue

def process_numbers(tasks_queue, results_list, list_lock):
    while True:
        try:
            number = tasks_queue.get(timeout=0.1)

            square = number ** 2

            with list_lock:
                results_list.append(square)

            tasks_queue.task_done()
        except queue.Empty:
            break

def main():
    tasks_queue = queue.Queue()
    results = []
    results_lock = threading.Lock()

    for i in range(1, 21):
        tasks_queue.put(i)

    threads = []

    for _ in range(4):
        thread = threading.Thread(
            target=process_numbers,
            args=(tasks_queue, results, results_lock)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(sorted(results))

if __name__ == "__main__":
    main()

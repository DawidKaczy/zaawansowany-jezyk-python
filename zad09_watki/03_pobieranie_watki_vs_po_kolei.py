import time
import threading
import random

def download_data(source_id):
    print(f"Rozpoczęto pobieranie ze źródła {source_id}...")
    sleep_time = random.uniform(0.5, 2.0)
    time.sleep(sleep_time)
    print(f"Zakończono pobieranie ze źródła {source_id} (trwało: {sleep_time:.2f}s).")

def run_sequential():
    print("\n--- WERSJA SEKWENCYJNA ---")
    start_time = time.time()

    for i in range(1, 11):
        download_data(i)

    duration = time.time() - start_time
    print(f"Czas całkowity (sekwencyjnie): {duration:.2f} sekund")
    return duration

def run_multithreaded():
    print("\n--- WERSJA WIELOWĄTKOWA ---")
    start_time = time.time()
    threads = []

    for i in range(1, 11):
        thread = threading.Thread(target=download_data, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    duration = time.time() - start_time
    print(f"Czas (wielowątkowo): {duration:.2f} sekund")
    return duration

def main():
    seq_time = run_sequential()
    mul_time = run_multithreaded()

    print("\n--- PODSUMOWANIE ---")
    print(f"Wersja sekwencyjna trwała: {seq_time:.2f}s")
    print(f"Wersja wielowątkowa trwała: {mul_time:.2f}s")

if __name__ == "__main__":
    main()



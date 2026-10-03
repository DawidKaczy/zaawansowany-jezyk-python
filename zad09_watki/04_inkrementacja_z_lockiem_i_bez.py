import threading

def increment_without_lock(shared_counter):
    for _ in range(50000):
        shared_counter[0] += 1


def increment_with_lock(shared_counter, lock):
    for _ in range(50000):
        with lock:
            shared_counter[0] += 1

def run_unsafe_version():
    counter = [0]
    threads = []

    for _ in range(20):
        thread = threading.Thread(target=increment_without_lock, args=(counter,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return counter[0]


def run_safe_version():
    counter = [0]
    lock = threading.Lock()
    threads = []

    for _ in range(20):
        thread = threading.Thread(target=increment_with_lock, args=(counter, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return counter[0]

def main():
    expected_result = 20 * 50000
    print(f"Spodziewany poprawny wynik: {expected_result}\n")

    unsafe_result = run_unsafe_version()
    print("--- WERSJA BEZ LOCK ---")
    print(f"Otrzymany wynik: {unsafe_result}")

    safe_result = run_safe_version()
    print("--- WERSJA Z LOCK ---")
    print(f"Otrzymany wynik: {safe_result}")

if __name__ == "__main__":
    main()
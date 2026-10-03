import threading

COUNTER = 0
counter_lock = threading.Lock()

def inc():
    global COUNTER
    for _ in range(10000):
        with counter_lock:
            COUNTER += 1


def main():
    threads = []
    for _ in range(5):
        t = threading.Thread(target=inc)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(COUNTER)

main()

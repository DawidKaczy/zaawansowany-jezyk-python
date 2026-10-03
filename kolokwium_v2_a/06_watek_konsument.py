import threading
import queue

def konsument(kolejka, wyniki, lock):
    while True:
        liczba = kolejka.get()
        if liczba is None:
            break

        kwadrat = liczba ** 2

        with lock:
            wyniki.append(kwadrat)

kolejka = queue.Queue()
wyniki = []
lock = threading.Lock()

for i in range(1, 21):
    kolejka.put(i)

for _ in range(4):
    kolejka.put(None)

watki = []
for _ in range(4):
    watek = threading.Thread(target=konsument, args=(kolejka, wyniki, lock))
    watki.append(watek)
    watek.start()

for watek in watki:
    watek.join()

print(wyniki)
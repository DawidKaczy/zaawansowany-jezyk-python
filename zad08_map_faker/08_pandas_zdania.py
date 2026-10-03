import pandas as pd

df = pd.read_csv('zdania.csv')

wyniki = []
for zdanie in df['zdanie']:
    liczba_slow = len(str(zdanie).split())
    wyniki.append((zdanie, liczba_slow))

wyniki_posortowane = sorted(wyniki, key=lambda x: x[1])

print(wyniki_posortowane)
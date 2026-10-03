
procenty = list(range(101))

def przelicz(p):
   if p < 50: return 2.0
   if p < 70: return 3.0
   if p < 85: return 4.0
   return 5.0

oceny_koncowe = list(map(lambda p: przelicz(p), procenty))

print(oceny_koncowe[0:51])
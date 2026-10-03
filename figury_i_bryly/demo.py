from figure import rectangle, triangle
from solid.bryla_obrotowa import kula, stozek, walec
from solid.wieloscian import  czworoscian, osmioscian, szescian
import solid


print("Trójkąt:")
print(f"Pole: {triangle.total_surface_area(10, 5)}")
print(f"Obwód: {triangle.perimeter(5, 5, 5)}")

print("Prostokąt:")
print(f"Pole: {rectangle.total_surface_area(3, 3)}")
print(f"Obwód: {rectangle.perimeter(5, 5)}")


print("\n")

print(f"Kula pole: {kula.pole_calkowite(4)}")
print(f"Kula objętość: {kula.objetosc(5)}")

print(f"Stożek pole: {stozek.pole_calkowite(3, 5)}")
print(f"Stożek objętość: {stozek.objetosc(3, 5)}")

print(f"Walec pole: {walec.pole_calkowite(4, 10)}")
print(f"Walec objętość: {walec.objetosc(4, 10)}")

# --- Wielościany ---
print(f"Sześcian pole: {szescian.pole_calkowite(3)}")
print(f"Sześcian objętość: {szescian.objetosc(3)}")

print(f"Czworościan pole: {czworoscian.pole_calkowite(4)}")
print(f"Czworościan objętość: {czworoscian.objetosc(4)}")

print(f"Ośmiościan pole: {osmioscian.pole_calkowite(5)}")
print(f"Ośmiościan objętość: {osmioscian.objetosc(5)}")

def sprawdz(funkcja):
    print("\n")
    print(f"Nazwa (.__name__): {funkcja.__name__}")
    print(f"Dokumentacja (.__doc__): {funkcja.__doc__}")
    print("Wywołanie help():")
    help(funkcja)
    print("-" * 40)

sprawdz(kula.pole_calkowite)
sprawdz(kula.objetosc)
sprawdz(stozek.pole_calkowite)
sprawdz(stozek.objetosc)
sprawdz(walec.pole_calkowite)
sprawdz(walec.objetosc)

def sprawdzv2():
    print(f"Lokalizacja pakietu 'solid': {solid.__file__}")
    print(f"Lokalizacja modulu 'kula': {kula.__file__}")

print(sprawdzv2())


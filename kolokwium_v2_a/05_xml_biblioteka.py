import xml.etree.ElementTree as ET

# 1. Wczytać plik XML i pobrać element główny
drzewo = ET.parse("biblioteka.xml")
korzen = drzewo.getroot()

# 2. Wyświetlić tytuły wszystkich książek
print("--- Tytuły wszystkich książek ---")
for ksiazka in korzen.findall('ksiazka'):
    tytul = ksiazka.find('tytul').text
    print(tytul)

# 3. Wyświetlić tylko książki z kategorii informatyka
print("\n--- Książki z kategorii informatyka ---")
for ksiazka in korzen.findall('ksiazka'):
    kategoria = ksiazka.find('kategoria').text
    if kategoria == "informatyka":
        tytul = ksiazka.find('tytul').text
        print(tytul)

# 4. Dodać nową książkę z atrybutem id="4" oraz podelementami
nowa_ksiazka = ET.SubElement(korzen, 'ksiazka', id="4")
ET.SubElement(nowa_ksiazka, 'tytul').text = "Podstawy sieci komputerowych"
ET.SubElement(nowa_ksiazka, 'autor').text = "Marek Nowakowski"
ET.SubElement(nowa_ksiazka, 'rok').text = "2024"
ET.SubElement(nowa_ksiazka, 'kategoria').text = "informatyka"

# 5. Zmienić rok książki o id="1" na 2026
for ksiazka in korzen.findall('ksiazka'):
    if ksiazka.get('id') == "1":
        ksiazka.find('rok').text = "2026"

# (Opcjonalnie) Sformatowanie XML, aby wcięciami przypominał oryginał (wymaga Pythona 3.9+)
if hasattr(ET, 'indent'):
    ET.indent(drzewo, space="    ", level=0)

# 6. Zapisać zmodyfikowany dokument do pliku z deklaracją XML i kodowaniem UTF-8
drzewo.write("biblioteka_zmieniona.xml", encoding="UTF-8", xml_declaration=True)
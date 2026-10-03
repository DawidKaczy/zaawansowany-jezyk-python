import xml.etree.ElementTree as ET

tree = ET.parse("studenci.xml")
root = tree.getroot()

for student in root.findall("student"):
    kierunek = student.find("kierunek").text
    if kierunek == "Informatyka":
        imie = student.find("imie").text
        nazwisko = student.find("nazwisko").text
        wiek = student.find("wiek").text
        print(f"Imię: {imie}, Nazwisko: {nazwisko}, Wiek: {wiek}")
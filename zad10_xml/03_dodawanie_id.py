import xml.etree.ElementTree as ET

def dodaj_id_do_xml():
    tree = ET.parse("studenci.xml")
    root = tree.getroot()

    for index, student in enumerate(root.findall("student"), start=1):
        student.set("id", str(index))

    if hasattr(ET, "indent"):
        ET.indent(root, space="    ", level=0)

    tree.write("studenci_z_id.xml", encoding="utf-8", xml_declaration=True)

def print_id():
    tree = ET.parse("studenci_z_id.xml")
    root = tree.getroot()

    for student in tree.findall("student"):
        id = student.get("id")
        imie = student.find("imie").text
        nazwisko = student.find("nazwisko").text
        wiek = student.find("wiek").text
        kierunek = student.find("kierunek").text

        print(f"id = {id}, imie = {imie}, nazwisko = {nazwisko}, wiek = {wiek}, kierunek = {kierunek}")

if __name__ == "__main__":
    dodaj_id_do_xml()
    print_id()
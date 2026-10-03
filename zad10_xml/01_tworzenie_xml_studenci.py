import xml.etree.ElementTree as ET

def create_students_xml():
    students_data = [
        {"imie": "Jan", "nazwisko": "Kowalski", "wiek": "21", "kierunek": "Informatyka"},
        {"imie": "Anna", "nazwisko": "Nowak", "wiek": "22", "kierunek": "Matematyka"},
        {"imie": "Piotr", "nazwisko": "Wiśniewski", "wiek": "20", "kierunek": "Automatyka"},
        {"imie": "Maria", "nazwisko": "Wójcik", "wiek": "23", "kierunek": "Fizyka"},
        {"imie": "Tomasz", "nazwisko": "Kamiński", "wiek": "21", "kierunek": "Mechatronika"}
    ]
    studenci = ET.Element("studenci")

    for data in students_data:
        student = ET.SubElement(studenci, "student")

        imie = ET.SubElement(student, "imie")
        imie.text = data["imie"]

        nazwisko = ET.SubElement(student, "nazwisko")
        nazwisko.text = data["nazwisko"]

        wiek = ET.SubElement(student, "wiek")
        wiek.text = data["wiek"]

        kierunek = ET.SubElement(student, "kierunek")
        kierunek.text = data["kierunek"]

    tree = ET.ElementTree(studenci)
    tree.write("studenci.xml", encoding="utf-8", xml_declaration=True)

def main():
    create_students_xml()
    tree = ET.parse("studenci.xml")
    root = tree.getroot()

    for student in tree.findall("student"):
        imie = student.find("imie").text
        nazwisko = student.find("nazwisko").text
        wiek = student.find("wiek").text
        kierunek = student.find("kierunek").text

        print(f"imie = {imie}, nazwisko = {nazwisko}, wiek = {wiek}, kierunek = {kierunek}")

if __name__ == "__main__":
    main()
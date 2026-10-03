import xml.etree.ElementTree as ET

tree = ET.parse("studenci.xml")
root = tree.getroot()

nowy_student = ET.SubElement(root, "student")
ET.SubElement(nowy_student, "imie").text = "Marek"
ET.SubElement(nowy_student, "nazwisko").text = "Zieliński"
ET.SubElement(nowy_student, "wiek").text = "22"
ET.SubElement(nowy_student, "kierunek").text = "Logistyka"

tree.write("studenci.xml", encoding="utf-8", xml_declaration=True)
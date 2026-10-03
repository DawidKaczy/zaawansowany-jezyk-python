import xml.etree.ElementTree as ET

tree = ET.parse("studenci_z_id.xml")
root = tree.getroot()

for student in root.findall("student"):
    if student.get("id") == "1":
        student.find("wiek").text = "25"

tree.write("studenci_zmienieni.xml", encoding="utf-8", xml_declaration=True)
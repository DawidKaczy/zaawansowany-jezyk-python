import xml.etree.ElementTree as ET

tree = ET.parse("studenci_z_id.xml")
root = tree.getroot()

for student in root.findall("student"):
    if student.get("id") == "3":
        root.remove(student)

tree.write("studenci_z_id.xml", encoding="utf-8", xml_declaration=True)
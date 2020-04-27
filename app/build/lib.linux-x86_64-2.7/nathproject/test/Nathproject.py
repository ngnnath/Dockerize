"""Main module."""
import json
import xml.etree.ElementTree as ET

class Nathproject:

    def createJSON(self):
        data_set = {"key1": [1, 2, 3], "key2": [4, 5, 6]}

        json_dump = json.dumps(data_set)
        return json_dump

    def readXMLFile(self):
        tree = ET.parse('file.xml')
        root = tree.getroot()
        return root


# tableau_to_powerbi_converter.py

import xml.etree.ElementTree as ET
import json
import os

class TableauToPowerBIConverter:
    def __init__(self, twb_file):
        self.twb_file = twb_file
        self.powerbi_structure = {
            "metadata": {
                "components": {}
            },
            "semanticModel": {},
            "report": {}
        }
        self.equivalents = {
            "Worksheet": "Page",
            "Dashboard": "Dashboard",
            "Measure": "CalculatedColumn",
            "Dimensi0on": "Field",
            "DataSource": "DataSet",
            # Add more mappings as necessary
        }
        self.log = []

    def log_components(self, tableau_component, powerbi_component):
        log_entry = f'Tableau Component: {tableau_component} => Power BI Component: {powerbi_component}'
        self.log.append(log_entry)

    def convert_components(self):
        tree = ET.parse(self.twb_file)
        root = tree.getroot()

        for component in root.iter('worksheet'):
            name = component.get('name')
            powerbi_component = self.equivalents.get("Worksheet", "Not Available")
            self.powerbi_structure["metadata"]["components"][name] = powerbi_component
            self.log_components("Worksheet", powerbi_component)

        for component in root.iter('dashboard'):
            name = component.get('name')
            powerbi_component = self.equivalents.get("Dashboard", "Not Available")
            self.powerbi_structure["metadata"]["components"][name] = powerbi_component
            self.log_components("Dashboard", powerbi_component)

        # Simulating additional conversion for Measures, Dimensions, etc.
        # This should be expanded based on actual needs from the TWB file structure.

    def create_folders_and_files(self):
        base_name = os.path.splitext(self.twb_file)[0]
        
        # Create folders
        os.makedirs(f"{base_name}2.report", exist_ok=True)
        os.makedirs(f"{base_name}2.semanticmodel", exist_ok=True)

        # Save a sample report structure
        with open(os.path.join(f"{base_name}2.report", "sample_report.json"), 'w') as report_file:
            json.dump({
                "pages": [{"name": "Page1", "visuals": []}],
                "bookmarks": []
            }, report_file, indent=4)

        # Save a sample semantic model structure
        with open(os.path.join(f"{base_name}2.semanticmodel", "sample_semantic_model.json"), 'w') as semantic_file:
            json.dump({
                "tables": [],
                "relationships": [],
                "measures": []
            }, semantic_file, indent=4)

    def save_output_files(self):
        pbip_file = os.path.splitext(self.twb_file)[0] + '1' + '.pbip'

        # Create the .pbip file using the current power BI structure
        with open(pbip_file, 'w') as pbip:
            json.dump(self.powerbi_structure, pbip, indent=4)

    def convert(self):
        self.convert_components()
        self.create_folders_and_files()
        self.save_output_files()
        print("\n".join(self.log))


if __name__ == "__main__":
    twb_input_file = "Sales Summary(Tableau) twbx.twb"  # Change this to your input TWB file
    converter = TableauToPowerBIConverter(twb_input_file)
    converter.convert()
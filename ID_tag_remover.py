import argparse
import re

def remove_id_from_xml(input_file, output_file):
    with open(input_file, 'r') as file:
        xml_content = file.readlines()

    updated_content = [line for line in xml_content if not re.search(r'<Id>\d+</Id>', line)]

    with open(output_file, 'w') as file:
        file.writelines(updated_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Remove lines with <Id> tags containing any number from an XML file.')
    parser.add_argument('input_file', type=str, help='Path to the input XML file')
    parser.add_argument('output_file', type=str, help='Path to the output XML file')
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file

    remove_id_from_xml(input_file, output_file)
    print(f"Lines with <Id> tags containing any number removed from {input_file}. Output saved to {output_file}.")

# This scripts print out all PDF files in a directory. 

import os
import subprocess

def print_pdf_with_acrobat(pdf_path, acrobat_path):
    # Command to print the PDF using Adobe Acrobat Reader
    command = f'"{acrobat_path}" /t "{pdf_path}"'
    print(f'Executing command: {command}')
    subprocess.run(command, shell=True)

def print_all_pdfs_in_directory(directory, acrobat_path):
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            file_path = os.path.join(directory, filename)
            print(f'Printing {file_path}')
            print_pdf_with_acrobat(file_path, acrobat_path)

if __name__ == "__main__":
    directory = '.'
    acrobat_path = 'C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe'
    print_all_pdfs_in_directory(directory, acrobat_path)

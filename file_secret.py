import zipfile
import datetime
import pyminizip

def zip_file(file_path, password):
    # Get the current date in the format YYYY-MM-DD
    date = datetime.date.today().strftime('%Y-%m-%d')
    # Open the file
    with open(file_path, 'rb') as file:
        # Create a ZIP file with the same name as the original file and the current date
        zip_path = f"{file_path[:5]}-{date}.zip"
        print("hehe",zip_path)
        # Create a new ZIP file with the desired name
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            # Set the password for the ZIP file
            zip_file.setpassword(password.encode('utf-8'))
            # Add the original file to the ZIP file
            zip_file.write(file_path, file_path.split('/')[-1])
            
    return zip_path

def zip_file2(file_path, password):
    # Get the current date in the format YYYY-MM-DD
    date = datetime.date.today().strftime('%Y-%m-%d')
    # Create a ZIP file with the same name as the original file and the current date
    zip_path = f"{file_path[:-5]}-{date}.zip"
    # Compress the file using pyminizip library
    pyminizip.compress(file_path, None, zip_path, password, 0)
    return zip_path

zip_file2("lakas.xlsx","boggancs")
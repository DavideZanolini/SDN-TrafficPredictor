import gdown
import zipfile
import os
import re

# Function to extract file_id from Google Drive URL
def extract_file_id(url):
    match = re.search(r'(?:/d/|id=|open\?id=|file/d/|drive.google.com/file/d/)([a-zA-Z0-9_-]+)', url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid Google Drive URL")

# Ask the user for the Google Drive file URL
file_url = input("Please enter the Google Drive file URL: ")

# Extract the file_id from the URL
try:
    file_id = extract_file_id(file_url)
except ValueError as e:
    print(e)
    exit()

# Construct the download URL
url = f'https://drive.google.com/uc?id={file_id}&export=download'

# Download the file using gdown
output = 'folder.zip'
gdown.download(url, output, quiet=False)

# Check if the downloaded file is a zip file
if zipfile.is_zipfile(output):
    # Extract the zip file
    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall('extracted_files')

    # Delete the zip file after extraction
    os.remove(output)
else:
    print("The downloaded file is not a zip file.")
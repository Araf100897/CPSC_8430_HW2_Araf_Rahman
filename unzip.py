import zipfile
import os

def unzip_file(zip_path, extract_to):
    """
    Unzips a .zip file to a specified directory.

    Parameters:
    zip_path (str): The path to the .zip file.
    extract_to (str): The directory where the files should be extracted.
    """
    if not os.path.exists(zip_path):
        print(f"The file {zip_path} does not exist.")
        return

    # Create the target directory if it doesn't exist
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Files extracted to: {extract_to}")

if __name__ == "__main__":
    zip_path = 'MLDS_hw2_1_data.zip'  # Replace with your .zip file path
    extract_to = 'MLDS_hw2_1'  # Replace with your extraction directory
    unzip_file(zip_path, extract_to)

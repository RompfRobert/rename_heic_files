import os
from datetime import datetime
import subprocess
import pyheif

def get_original_creation_time(file_path):
    try:
        # Use pyheif to open the HEIC image
        heif_image = pyheif.read(file_path)
        
        # Use exiftool to extract EXIF data
        result = subprocess.run(['exiftool', '-CreateDate', '-j', file_path], stdout=subprocess.PIPE, text=True)
        exif_data = result.stdout

        if exif_data:
            # Extract the creation time from the exiftool output
            exif_dict = eval(exif_data)
            creation_time_str = exif_dict[0]['CreateDate']
            return datetime.strptime(creation_time_str, "%Y:%m:%d %H:%M:%S")
        
        # If EXIF data doesn't contain creation time, use file creation time
        return datetime.fromtimestamp(os.path.getctime(file_path))
    except Exception as e:
        print(f"Error extracting creation time from HEIC file {file_path}: {e}")
        # Use file creation time in case of any error
        return datetime.fromtimestamp(os.path.getctime(file_path))

def rename_images_in_folder(folder_path):
    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print(f"Error: The folder {folder_path} does not exist.")
        return

    # List all files in the folder
    file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Process each image in the folder
    for image_file_name in file_list:
        image_file_path = os.path.join(folder_path, image_file_name)
        rename_image(image_file_path)

def rename_image(file_path):
    # Get the original creation time of the image
    creation_time = get_original_creation_time(file_path)
    
    # Format the date and time as needed (you can customize the format)
    formatted_time = creation_time.strftime("%Y%m%d_%H%M%S")
    
    # Get the file extension
    _, file_extension = os.path.splitext(file_path)
    
    # Create the new file name
    new_file_name = f"IMG_{formatted_time}{file_extension}"
    
    # Get the directory of the file
    file_directory = os.path.dirname(file_path)
    
    # Create the new file path
    new_file_path = os.path.join(file_directory, new_file_name)
    
    try:
        # Rename the file
        os.rename(file_path, new_file_path)
        print(f"File {file_path} renamed successfully. New file name: {new_file_name}")
    except Exception as e:
        print(f"Error renaming the file {file_path}: {e}")

# Example usage
folder_path = "img"
rename_images_in_folder(folder_path)

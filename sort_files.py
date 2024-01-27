import os
import shutil

def sort_files_by_extension(folder_path):
    # Iterate through all files in the specified folder
    for filename in os.listdir(folder_path):
        # Get the full path of the file
        file_path = os.path.join(folder_path, filename)

        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Get the file extension
            _, file_extension = os.path.splitext(filename)
            file_extension = file_extension.lower()

            # Create a folder with the extension name if it doesn't exist
            target_folder = os.path.join(folder_path, file_extension[1:])
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            # Move the file to the corresponding folder
            shutil.move(file_path, os.path.join(target_folder, filename))

if __name__ == "__main__":
    # Specify the folder path where your files are located
    folder_to_sort = "img"

    # Call the function to sort files
    sort_files_by_extension(folder_to_sort)

    print("Files sorted successfully.")

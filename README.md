# Image Renaming Script Documentation

## Overview

This Python script is designed to rename image files within a specified folder, preserving the original creation time information from the image metadata. The script primarily targets HEIC (High Efficiency Image Format) files and uses the `pyheif` library to extract creation time information. In case the metadata extraction fails, it falls back to using the file's creation time.

## Dependencies

Before running the script, ensure that the following dependencies are installed:

- `pyheif`: A Python library for reading HEIF files.
  ```bash
  pip install pyheif
  ```

- `exiftool`: A command-line tool for reading and writing metadata in image files. It is used to extract creation time information.
  - Download and install `exiftool` from [https://exiftool.org/](https://exiftool.org/).

## Usage

1. **Prepare Images:**
   Place the images you want to rename in a folder. For example, create a folder named "img" in the same directory as the script and place the images inside.

2. **Run the Script:**
   Execute the script by providing the path to the folder containing the images. For example, if the images are in a folder named "img," run the script as follows:
   ```bash
   python script_name.py
   ```

3. **Output:**
   The script will process each image within the specified folder, extracting the creation time from the image metadata or using the file's creation time. It will then rename each image with a new filename format: `IMG_YYYYMMDD_HHMMSS.ext`.

   - `YYYYMMDD`: Year, month, and day of creation.
   - `HHMMSS`: Hour, minute, and second of creation.
   - `ext`: Original file extension.

   The renamed images will be in the same folder as the original images.

## Functions

### `get_original_creation_time(file_path)`

- **Parameters:**
  - `file_path` (str): Path to the image file.

- **Returns:**
  - `datetime`: Original creation time extracted from the image metadata or file creation time.

- **Description:**
  Attempts to extract the original creation time of the image from the metadata using the `pyheif` library. If unsuccessful, it falls back to using the file's creation time.

### `rename_image(file_path)`

- **Parameters:**
  - `file_path` (str): Path to the image file.

- **Description:**
  Renames the given image file by appending the original creation time to the filename in the format specified. The renamed file is saved in the same directory.

### `rename_images_in_folder(folder_path)`

- **Parameters:**
  - `folder_path` (str): Path to the folder containing the images.

- **Description:**
  Processes all image files in the specified folder by calling the `rename_image` function for each file.

### Example Usage:

```python
# Example usage
folder_path = "img"
rename_images_in_folder(folder_path)
```

This function can be customized for specific folder paths or integrated into larger scripts as needed.

---

Feel free to customize the documentation further based on your specific requirements or additional features in your script.

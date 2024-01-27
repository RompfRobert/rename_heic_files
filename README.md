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

# Set up SSH Connection Between Linux and GitHub (Ubuntu) 

Setting up an SSH connection between your Linux machine and GitHub involves generating an SSH key pair, adding the public key to your GitHub account, and configuring your local SSH agent. Here's a step-by-step guide:

### Step 1: Check for Existing SSH Keys

Before generating a new SSH key, check if you already have one:

```bash
ls -al ~/.ssh
```

Look for files named `id_rsa` (private key) and `id_rsa.pub` (public key). If they exist, you can use them. If not, proceed to the next step.

### Step 2: Generate a New SSH Key

Run the following command to generate a new SSH key pair:

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

Replace "your_email@example.com" with the email associated with your GitHub account. Press Enter to accept the default file location (`~/.ssh/id_rsa`) and enter a passphrase (optional).

### Step 3: Add SSH Key to SSH Agent

Run the following commands to add the SSH private key to the SSH agent:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

### Step 4: Add SSH Key to GitHub

Copy the SSH public key to your clipboard:

```bash
cat ~/.ssh/id_rsa.pub
```

Go to your GitHub account -> Settings -> SSH and GPG keys -> New SSH Key, and paste the copied key.

### Step 5: Test the Connection

Run the following command to test the connection:

```bash
ssh -T git@github.com
```

You may see a message about authenticity. Type "yes" to confirm. If everything is set up correctly, you should see a message indicating a successful authentication.

### Optional: Configuring SSH Hosts (if using multiple accounts)

If you have multiple GitHub accounts, you can configure SSH hosts in your `~/.ssh/config` file. For example:

```bash
Host github.com
   HostName github.com
   User git
   IdentityFile ~/.ssh/id_rsa

Host github-other-account
   HostName github.com
   User git
   IdentityFile ~/.ssh/id_rsa_other_account
```

Replace "other-account" and "id_rsa_other_account" with your specific account details.

Now you should have a working SSH connection between your Linux machine and GitHub.

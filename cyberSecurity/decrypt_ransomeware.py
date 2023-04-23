import os

# Define the directory to decrypt
target_directory = "C:/Users/91821/Documents/GitHub/python-my-projects"

# Define the file extension to decrypt
file_extension = ".txt"

# Decrypt the files in the target directory
for root, dirs, files in os.walk(target_directory):
    for file in files:
        if file.endswith(file_extension):
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                data = f.read()
            with open(file_path, "wb") as f:
                f.write(data[::-1])
            with open(file_path, "r") as f:
                contents = f.read()
            contents = contents.replace("Your files have been encrypted! Send 1 Bitcoin to 123ABC to get the decryption key.", "")
            with open(file_path, "w") as f:
                f.write(contents)

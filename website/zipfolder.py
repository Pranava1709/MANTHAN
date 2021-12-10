import os
import zipfile


def zip_directory(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, mode='w') as zipf:
        len_dir_path = len(folder_path)
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, file_path[len_dir_path:])


# zip_directory('Single-Image-Dehazing-Python\\result', '.\\result.zip')
# zip_directory('Single-Image-Dehazing-Python\\output', '.\\output.zip')

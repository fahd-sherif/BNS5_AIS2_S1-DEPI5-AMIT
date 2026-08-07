import os
import random

def thanos_project(folder_path: str, num_files: int) -> None:
    """
    Create a folder, generate a number of text files,
    then randomly delete half of them (Thanos snap).
    param folder_path: The name or path of the folder to create.
    type folder_path: str
    param num_files: The number of text files to generate.
    type num_files: int
    return: None
    rtype: None
    """
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    for i in range(1, num_files + 1):
        file_name = f"file_{i}.txt"
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "w") as file:
            file.write(f"This is file number {i}")
    files = os.listdir(folder_path)
    print("Files before delete:")
    print(files)
    print("Number of files:", len(files))
    random_files = random.sample(files, len(files) // 2)
    for file in random_files:
        os.remove(os.path.join(folder_path, file))
    remaining_files = os.listdir(folder_path)
    print("\nDeleted files:")
    print(random_files)
    print("\nRemaining files:")
    print(remaining_files)
    print("Number of remaining files:", len(remaining_files))

folder: str = input("Enter folder name: ")
number: int = int(input("Enter number of files: "))

thanos_project(folder, number)
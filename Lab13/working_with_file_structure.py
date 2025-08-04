import os


root_path = os.path.dirname(os.path.abspath(__file__))
print(root_path)

DONWLOAD_PATH = os.path.join(root_path, "downloads")
# try:
#     os.chdir(root_path)
# except FileNotFoundError:
#     print(f"Folder {root_path} did not exists!")
#     sys.exit()


# cwd = os.getcwd()
# print("Current working directory:", cwd)
print(os.listdir("."))

os.mkdir(DONWLOAD_PATH)

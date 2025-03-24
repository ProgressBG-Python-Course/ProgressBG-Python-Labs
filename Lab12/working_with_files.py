# # raws strings
# print("C:\\Users\\Username\\Documents\\example.txt")
# print(r"C:\Users\Username\Documents\example.txt")

# documents_path = r"C:\Users\Username\Documents"


# import os

# cwd = os.getcwd()
# print("Current Working Directory:", cwd)  #

# file_path = __file__
# dir_path = os.path.dirname(file_path)

# # print(f"File path: {file_path}")
# print(f"Dir path: {dir_path}")
# os.chdir(dir_path)

# print(f"CWD now: {os.getcwd()}")

# import os

# # docs_path = r"C:\User\Documents"
# # file_name = r"file.txt"

# # print(docs_path + file_name)
# # print(os.path.join(docs_path, file_name))


# import os

# print(os.path.exists("sys.py"))
# print(os.path.exists("sy.py"))


# --------------------------- Working with folders --------------------------- #
import os

# print(os.listdir(os.getcwd()))

# try:
#     os.makedirs("./FolderC/Folder1")
# except FileExistsError:
#     print("File exists")


# os.rmdir("C:\\")


# def create_folder(folder_name):
#     if os.path.exists(folder_name):
#         return
#     os.mkdir(folder_name)


# docs_path = "Documents"
# create_folder(docs_path)


# --------------------------- Working with files`` --------------------------- #
import os

f = open("./FolderA/file1.txt", mode="r")
print(f.readlines())

f.close()

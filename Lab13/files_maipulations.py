# --------------------------------- Open file -------------------------------- #
# f = open("exmaple.txt", "w")
# f.write("Some content")
# f.close()

# with open("exmaple.txt", "w") as f:
#     f.write("Some content")
# # autimatically closes f


# try:
#     with open("example.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("File not found!")
# except PermissionError:
#     print("Permission denied!")
# except Exception as e:
#     print(f"Unexpected error: {e}")

# ------------------------------ Read from file ------------------------------ #
# with open("exmaple.txt") as f:
# content = f.read(4)
# line1 = f.readline()
# line2 = f.readline()
# print(line1)
# print(line2)

# lines = f.readlines()
# lines = [line.strip() for line in lines]
# for line in lines:
#     print(line.upper())

# for line in f:
#     print(line.strip().upper())


# ------------------------------- write in file ------------------------------ #
# with open("example.txt", "w") as f:
#     f.write("""
#     new line 1
#     new line 2
#             """)


# data = ["Hello, world!", "This is a new line."]
# with open("example.txt", "a") as f:
#     f.writelines(data)


# -------------------------------- remove file ------------------------------- #
# import os

# try:
#     os.remove("./example.txt")
# except FileNotFoundError as e:
#     print("File did not exist!", e)
# except Exception as e:
#     print("ups, someting went wrong!")

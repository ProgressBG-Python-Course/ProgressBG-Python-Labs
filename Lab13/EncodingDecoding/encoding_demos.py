# with open("./example.txt", "w", encoding="windows-1251") as f:
#     f.write("ютия")


# print(ord("я"))
# # 1103
# print(chr(1103))
# # я


# --------------------------------- encode() --------------------------------- #
# string = "123abc"

# bytes_string = string.encode(encoding="utf-8")

# print("Byte object:", bytes_string)
# print("Type: ", type(bytes_string))
# print("Length:", len(bytes_string))

byte_string = b"\xd0\xb0\xd0\xb1\xd0\xb2"
string = byte_string.decode()


print("String object:", string)
print("Type: ", type(string))
print("String length:", len(string))
print("Byte_string length:", len(byte_string))

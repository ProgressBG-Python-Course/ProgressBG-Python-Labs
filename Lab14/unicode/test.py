# name = "Ada"
# print(ord("A"))
# print(ord("d"))
# print(ord("a"))
# print(ord("😄"))

# print(chr(128516))


# ---------------------------------- encode ---------------------------------- #
# string = "😄"

# bytes_string = string.encode(encoding="utf-8")

# print("Byte object:", bytes_string)
# print("Type: ", type(bytes_string))
# print("Length:", len(bytes_string))


# # Byte object: b'123\xd0\xb0\xd0\xb1\xd0\xb2'
# # Type:  <class 'bytes'>
# # Length: 9


# text = "Здравей, свят!"
# try:
#     ascii_encoded = text.encode("ascii")
#     print("ASCII Encoded:", ascii_encoded)
# except UnicodeEncodeError as e:
#     print("Error:", e)

# # Error: 'ascii' codec can't encode characters in position 0-6: ordinal not in range(128)


# ---------------------------------- decode ---------------------------------- #
byte_string = b"\xd0\xb0\xd0\xb1\xd0\xb2"
string = byte_string.decode()


print("String object:", string)
print("Type: ", type(string))
print("Type: ", type(byte_string))
print("String length:", len(string))
print("Byte_string length:", len(byte_string))

# String object: абв
# Type:  <class 'str'>
# String length: 3
# Byte_string length: 6

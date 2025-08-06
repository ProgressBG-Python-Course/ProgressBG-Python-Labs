# print(f"Current working directory: {os.getcwd()}")

# file = open("./user_data.txt", mode="r", encoding="None")


# user_name = "Ada"
# # f = open("./user_data.txt", mode="a", encoding="utf-8")
# # f.write(user_name)
# # f.close()

users = []

with open("./user_data.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        row_words = line.strip().split(" ")
        users.extend(row_words)


print(users)  # []

# import re

# # Match any vowel character
# matched = re.findall(r"[aeiouy]", "astroid")
# print(matched)


# # Match any non-vowel character
# matched = re.findall(
#     r"[^aeiouy]",
#     """astr
#                      oid""",
# )
# print(matched)

# # match any digit or hyphen:
# matched = re.findall("[0-9-]", "a2-b8")
# print(matched)


# Task: validate user name:
# 1. at least 3 symbols
# 2. letters, digit

# Positive: "ivan", "ivan1234", "1234ivan"
# Negative: "iv",  "ivan1234!", "123+"

# import re

# test_names = ["ivan", "ivan1234", "1234ivan", "iv", "ivan1243!", "123+"]

# pattern = r"^[a-zA-Z0-9]{3,}$"

# for user_name in test_names:
#     m = re.match(pattern, user_name)
#     if m:
#         print(f"{user_name} is valid!")
#     else:
#         print(f"{user_name} is INVALID!")


# ------------------------------ Word bounderies ----------------------------- #
# import re

# pattern = r"\babc\b"
# tests = [
#     "!!!",  # no
#     "abc",  # yes
#     "1abc1",  # no
#     "@abc@",  # yes
#     "_abc2",  # no
# ]

# for test in tests:
#     m = re.search(pattern, test)
#     if m:
#         print(f"{test} - yes")
#     else:
#         print(f"{test} - no")


# ----------------------------------- Flags ---------------------------------- #
# import re

# ### eXtended (x)
# pattern = r"""
# \w+ # match [a-bA-B0-9_] at least 1
# \d* # match 0 or more digits
# """

# test_string = "abc"
# m = re.search(pattern, test_string, re.X)
# print(m)


# -------------------- Capturing and Non-Capturing groups -------------------- #
# import re

# test = """
#  maria:+3598765432
# # georgi:+229876543
#  elena: +4597654321
#  petar:+3596543210
#  viktor:+3595432109
# """

# # Using capturing group to get names and ages
# pattern = re.compile(r"^.*?([a-z]+):\s?\+359(\d{7})$", re.MULTILINE)
# matches = pattern.findall(test)

# for match in matches:
#     print(match[0])
#     print(match[1])


# --------------------------- Using regex in Python -------------------------- #
# import re

# text = "ABRACADABRA"
# pattern = r"aca"

# # regex = re.compile(pattern, re.I)

# # if regex.search(text):
# #     print("Match")


# if re.match(pattern, text, re.I):
#     print("Match")
# else:
#     print("No match")


# import re

# text = """cats
# dogs"""

# regex = re.compile(r"(?:cat|dog)s")

# matches = regex.findall(text)
# print(matches)


import re


text = """
there is a lots of cats and dogs. And a cat is a dog. Acatoio
"""

regex = re.compile(r"\b(?:cat|dog)")
replaced_text = regex.sub("@@@", text)
print(replaced_text)

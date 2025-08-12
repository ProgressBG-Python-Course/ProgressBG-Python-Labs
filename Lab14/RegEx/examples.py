# import re

# # The text containing various phone numbers
# text = """
# Contact us at +359 888-123-456 for support.
# Our main office line is +359 2-987-6543 (this won't match our specific pattern).
# You can also reach us via mobile at +359 899-000-111 or +359 876-543-210.
# An invalid number: 123-456-7890.
# Another invalid number: +359 88-123-456.
# """

# # The regular expression pattern for +359 phone numbers formatted as +359 XXX-XXX-XXX
# # - \+ : Matches a literal plus sign (it's escaped because + is a special character in regex)
# # - 359 : Matches the literal digits '359'
# # - \s : Matches any whitespace character (like space)
# # - \d{3} : Matches exactly three digits (0-9)
# # - - : Matches a literal hyphen
# phone_pattern = r"\+359\s\d{3}-\d{3}-\d{3}"

# print("Searching for phone numbers with the pattern: " + phone_pattern)
# print("-" * 50)
# print(f"Original text:\n{text}")
# print("-" * 50)

# # Find all occurrences of the pattern in the text
# # re.findall() returns a list of all non-overlapping matches
# found_numbers = re.findall(phone_pattern, text)

# if found_numbers:
#     print("Found phone numbers:")
#     for number in found_numbers:
#         print(f"- {number}")
# else:
#     print("No matching phone numbers found.")

# print("-" * 50)

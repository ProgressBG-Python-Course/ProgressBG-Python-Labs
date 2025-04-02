import re

text = "Name: Maria, Age: 30"
pattern = r"Name: (\w+), Age: (\d+)"  # Capture name and age

match = re.search(pattern, text)

if match:
    print("Full match:", match.group(0))
    print("Name (Group 1):", match.group(1))
    print("Age (Group 2):", match.group(2))
    print("Age (Group 2):", match.group(3))
    print("All groups:", match.groups())

# OUTPUT
# Full match: Name: Maria, Age: 30
# Name (Group 1): Maria
# Age (Group 2): 30
# All groups: ('Maria', '30')

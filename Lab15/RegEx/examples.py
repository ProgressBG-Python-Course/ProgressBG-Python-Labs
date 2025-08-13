# print("a(\\t+)a")
# print(r"a(\t+)a")

import re

regex_string = r"a(\d+)([a-z]+)"
rx = re.compile(regex_string)

test_string = "a23434343atata"

m = rx.search(test_string)

if m:
    print(m.group(1))
    print(m.group(2))
else:
    print("No match!")

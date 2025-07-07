import time

# Creating a large set and list for demonstration
large_set = set(range(10_000_000))
large_list = list(range(10_000_000))

# Searching for an element in the set
start_time = time.time()
exists_in_set = 999999 in large_set     # Searching for a high number
set_duration = time.time() - start_time

# Searching for the same element in the list
start_time = time.time()
exists_in_list = 999999 in large_list  # Searching for the same high number
list_duration = time.time() - start_time

print(f"Time taken for search in set: {set_duration:.8f} seconds")
print(f"Time taken for search in list: {list_duration:.8f} seconds")

# Time taken for search in set: 0.00000381 seconds
# Time taken for search in list: 0.01182604 seconds
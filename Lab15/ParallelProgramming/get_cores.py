import psutil

# Get the number of physical cores
physical_cores = psutil.cpu_count(logical=False)
print(f"Number of physical cores: {physical_cores}")

# Get the number of logical processors (hardware threads)
logical_processors = psutil.cpu_count(logical=True)
print(f"Number of logical processors (hardware threads): {logical_processors}")

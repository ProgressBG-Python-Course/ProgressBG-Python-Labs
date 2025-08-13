import sys

print(sys.argv)

x = sys.argv[1]
y = sys.argv[2]
# y = args2
print(f"{x} + {y} = {x + y} ")

if sys.argv[1] == "--help":
    print("Usage: pythxon sys_demxo.py [options]")
elif sys.argv[1] == "--version":
    print("sys_demo.py version 1.0")

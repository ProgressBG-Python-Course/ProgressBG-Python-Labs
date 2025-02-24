import numpy

# lets create a python list
m = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

# create a numpy array from that list:
arr = numpy.array(m)
print(arr)

# now we can easily use numpy's multi-dim slicing:
print(arr[:,1])
#[2 5 8]

print(type(arr[:,1]))
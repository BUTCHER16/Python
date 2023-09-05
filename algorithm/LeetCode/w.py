import numpy

# Read input dimensions
n, m = map(int, input().split())

matrices=[]
# Read the matrix
for i in range(n):
    
    N = list(map(int, input().split()))
    matrices.append(N)

my_array = numpy.array(matrices)
print(numpy.transpose(my_array))
print(my_array.flatten())
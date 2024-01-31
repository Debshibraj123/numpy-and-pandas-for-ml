import numpy as np
# # a = np.array([2,1, 3, 4, 5, 6])

# # np.sort(a)
# # # print(a)

# # a2 = np.array([[2,1, 3, 4, 5, 6], [2,1, 3, 4, 5, 6]])

# # # print(a2.ndim)


# # ar_zero = np.zeros(4)
# # ar_zero1 = np.zeros((3, 4))
# # print(ar_zero)
# # print(ar_zero1)

# #to generate random array

# # var1 = np.random.rand(4)
# # print(var1)
# # var1 = np.random.rand(2, 5)
# # print(var1)
# # print(np.random.randint(min, max))



# # Data Type In Numpy Array
# # Using dtype we can find the type of numpy array

# # Arithmetic Operation In Numpy Array
# #https://www.youtube.com/watch?v=clbZakCzRWY&list=PLjVLYmrlmjGfgBKkIFBkMNGG7qyRfo00W&index=8

# #Access Array Elements
# # Array indexing is the same as accessing an array element.

# # You can access an array element by referring to its index number.

# # The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

# # ExampleGet your own Python Server
# # Get the first element from the following array:

# # import numpy as np

# # arr = np.array([1, 2, 3, 4])

# # print(arr[0])
# # Example
# # Get the second element from the following array.

# # import numpy as np

# # arr = np.array([1, 2, 3, 4])

# # print(arr[1])
# # Example
# # Get third and fourth elements from the following array and add them.

# # import numpy as np

# # arr = np.array([1, 2, 3, 4])

# # print(arr[2] + arr[3])
# # ADVERTISEMENT


# Access 2-D Arrays
# To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.

# Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.

# Example
# Access the element on the first row, second column:

# import numpy as np

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('2nd element on 1st row: ', arr[0, 1])
# Example
# Access the element on the 2nd row, 5th column:

# import numpy as np

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('5th element on 2nd row: ', arr[1, 4])
# Access 3-D Arrays
# To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.

# Example
# Access the third element of the second array of the first array:

# import numpy as np

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(arr[0, 1, 2])
# Example Explained
# arr[0, 1, 2] prints the value 6.

# And this is why:

# The first number represents the first dimension, which contains two arrays:
# [[1, 2, 3], [4, 5, 6]]
# and:
# [[7, 8, 9], [10, 11, 12]]
# Since we selected 0, we are left with the first array:
# [[1, 2, 3], [4, 5, 6]]

# The second number represents the second dimension, which also contains two arrays:
# [1, 2, 3]
# and:
# [4, 5, 6]
# Since we selected 1, we are left with the second array:
# [4, 5, 6]

# The third number represents the third dimension, which contains three values:
# 4
# 5
# 6
# Since we selected 2, we end up with the third value:
# 6

# Negative Indexing
# Use negative indexing to access an array from the end.

# Example
# Print the last element from the 2nd dim:

# import numpy as np

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('Last element from 2nd dim: ', arr[1, -1])
# Slicing arrays
# Slicing in python means taking elements from one given index to another given index.

# We pass slice instead of index like this: [start:end].

# We can also define the step, like this: [start:end:step].

# If we don't pass start its considered 0

# If we don't pass end its considered length of array in that dimension

# If we don't pass step its considered 1

# ExampleGet your own Python Server
# Slice elements from index 1 to index 5 from the following array:

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[1:5])
# Note: The result includes the start index, but excludes the end index.

# Example
# Slice elements from index 4 to the end of the array:

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[4:])
# Example
# Slice elements from the beginning to index 4 (not included):

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[:4])
# ADVERTISEMENT

# Negative Slicing
# Use the minus operator to refer to an index from the end:

# Example
# Slice from the index 3 from the end to index 1 from the end:

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[-3:-1])
# STEP
# Use the step value to determine the step of the slicing:

# Example
# Return every other element from index 1 to index 5:

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[1:5:2])



# Shape of an Array
# The shape of an array is the number of elements in each dimension.

# Get the Shape of an Array
# NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.

# ExampleGet your own Python Server
# Print the shape of a 2-D array:

# import numpy as np

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# print(arr.shape)
# The example above returns (2, 4), which means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 4.

# Example
# Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:

# import numpy as np

# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('shape of array :', arr.shape)
# What does the shape tuple represent?
# Integers at every index tells about the number of elements the corresponding dimension has.

# In the example above at index-4 we have value 4, so we can say that 5th ( 4 + 1 th) dimension has 4 elements.




# NumPy Array Iterating
# Iterating Arrays
# Iterating means going through elements one by one.

# As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.

# If we iterate on a 1-D array it will go through each element one by one.

# ExampleGet your own Python Server
# Iterate on the elements of the following 1-D array:

# import numpy as np

# arr = np.array([1, 2, 3])

# for x in arr:
#   print(x)
# Iterating 2-D Arrays
# In a 2-D array it will go through all the rows.

# Example
# Iterate on the elements of the following 2-D array:

# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6]])

# for x in arr:
#   print(x)
# If we iterate on a n-D array it will go through n-1th dimension one by one.

# To return the actual values, the scalars, we have to iterate the arrays in each dimension.

# Example
# Iterate on each scalar element of the 2-D array:

# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6]])

# for x in arr:
#   for y in x:
#     print(y)

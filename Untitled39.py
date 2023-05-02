#!/usr/bin/env python
# coding: utf-8

# 1.Write a Python Program to find sum of array?

# In[1]:


arr = [1, 2, 3, 4, 5]
array_sum = sum(arr)
print("Sum of array elements:", array_sum)


# 2.Write a Python Program to find largest element in an array?

# In[2]:


arr = [5, 8, 3, 9, 2]
largest = arr[0]
for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]
print("The largest element in the array is:", largest)


# 3.Write a Python Program for array rotation?

# In[3]:


def rotate_array(arr, d):
    n = len(arr)
    d = d % n
    arr[:] = arr[d:] + arr[:d]
arr = [1, 2, 3, 4, 5]
rotate_array(arr, 2)
print(arr) 


# 4.Write a Python Program to Split the array and add the first part to the end?

# In[4]:


def split_and_add(arr, n):
    part1 = arr[:n]
    part2 = arr[n:]
    result = part2 + part1
    return result
arr = [2, 3, 4, 5, 6]
n = 2
result = split_and_add(arr, n)
print(result)


# 5.Write a Python Program to check if given array is Monotonic?

# In[7]:


def is_monotonic(arr):
    return (all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or
            all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)))
arr1 = [1, 2, 3, 4, 5]  # Monotonically increasing
arr2 = [5, 4, 3, 2, 1]  # Monotonically decreasing
arr3 = [1, 2, 3, 2, 1]  # Not monotonic
print(is_monotonic(arr1)) 
print(is_monotonic(arr2)) 
print(is_monotonic(arr3)) 


# In[ ]:





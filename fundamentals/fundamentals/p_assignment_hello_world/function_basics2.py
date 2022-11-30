# def count_down(num):
#     newlist=[]
#     for i in range(num,-1,-1):
#         newlist.append(i)
#     return newlist

# print(count_down(5))

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

# def print_return(list):
#     print(list[0])
#     return list[1]

# print_return([1,2])
# print(print_return([1,2]))

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

# def first_plus_length(list):
#     sum=list[0]+len(list)
#     print(sum)
#     return sum
# first_plus_length([1,2,3,4,5])


# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

# def values_greater_than_second(list):
#     if len(list)<2:
#         return False
#     else:
#         count=0
#         newlist=[]
#         # print(len(list))
#         for i in range(len(list)):
#             if list[i]>list[1]:
#                 # print(i)
#                 count+=1
#                 newlist.append(list[i])
#         print(count)
#         return newlist

# values_greater_than_second([5,2,3,2,1,4])
# print(values_greater_than_second([5,2,3,2,1,4]))
# print(values_greater_than_second([3]) )


# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

# def size_and_value(num1,num2):
#     list=[]
#     for i in range(num1):
#         list.append(num2)
#     return list

# print(size_and_value(4,7))

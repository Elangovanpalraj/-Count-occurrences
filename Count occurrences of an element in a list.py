# Count occurrences of an element in a list
# ---------------------------------------\n
'''
Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10], x = 10
Output: 3 
Explanation: 10 appears three times in given list.
Input: lst = [8, 6, 8, 10, 8, 20, 10, 8, 8], x = 16
Output: 0
Explanation: 16 appears zero times in given list.
'''
# type
# ----\n
# Using a loop in Python
# Using List Comprehension
# Using enumerate function
# Using count()
# Using Counter()
# Using countOf()
# Using dictionary comprehension
# Using Pandas’s Library
# -------------------------------------------------------\n
# loop in python
# -------------\n
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
 
 
# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x,
                                        countX(lst, x)))
print(' ')

#  list comprehension
# ------------------\n
l = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5] 
ele=1
x=[i for i in l if i==ele] 
print("the element",ele,"occurs",len(x),"times")
print(' ')

#  enumerate function
# --------------------
l = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5] 
ele=1
x=[i for j,i in enumerate(l) if i==ele] 
print("the element",ele,"occurs",len(x),"times")
print(' ')
# element using count()
# ---------------------\n
# Python code to count the number of occurrences
def countX(lst, x):
    return lst.count(x)
 
 
# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, 
                                        countX(lst, x)))
print(' ')
# using Counter()
# ---------------\n
from collections import Counter
 
# declaring the list
l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
 
# driver program
x = 3
d = Counter(l)
print('{} has occurred {} times'.format(x, d[x]))
print(' ')
# Operator.countOf()
# ------------------\n
import operator as op
 
# declaring the list
l = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]
 
# driver program
x = 2
print(f"{x} has occurred {op.countOf(l, x)} times")
print(' ')
#  Dictionary Comprehension
# -------------------------\n
lis = ['a', 'd', 'd', 'c', 'a', 'b', 'b', 'a', 'c', 'd', 'e']
occurrence = {item: lis.count(item) for item in lis}
print(occurrence.get('e'))
print(' ')
# Using the Pandas library
# ----------------------\n
import pandas as pd
 
# declaring the list
l = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]
 
count = pd.Series(l).value_counts()
print("Element Count")
print(count)
print(' ')
# -----------------------\n































































































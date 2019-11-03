import pandas as pd
import numpy as np


"""

data = np.array(['a','b','c','d'])
s = pd.Series(data)
print("Series is\n", s)
print("Type is ", type(s))

series_with_index = pd.Series(data, index=[100, 101, 102, 103])
print("Series with index is\n", series_with_index)


data = {'a' : 0., 'b' : 1., 'c' : 2.}
series_with_dict = pd.Series(data)
print("Series with dict is\n", series_with_dict)


data = {'a' : 0., 'b' : 1., 'c' : 2.}
series_with_dict_i = pd.Series(data, index=['b','c','d','a'])
print("Series with dict i\n", series_with_dict_i)


series_with_scalar = pd.Series(5, index=[0, 1, 2, 3])
print("Series with scalar is\n", series_with_scalar)
"""
#Accessing Data from Series with Position

s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
#retrieve the first element
print("First element is\n", s[0])

#retrieve the first three element
print("First three elements are\n", s[:3])

#retrieve the last three element
print("Last three elements are\n", s[-3:])

#Retrieve Data Using Label (Index)
#retrieve a single element
print("Single element using lable(Index)\n", s['a'])


#retrieve a multiple elements
print("Multiple element using lable(Index))\n", s[['a','c','d']])

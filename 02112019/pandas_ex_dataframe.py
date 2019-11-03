import pandas as pd

data = [1,2,3,4,5]
df = pd.DataFrame(data)
print("Table frame is\n", df)


data1 = [['Alex',10],['Bob',12],['Clarke',13]]
df1 = pd.DataFrame(data1, columns=['Name','Age'])
print("DF1", df1)


data2 = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df2 = pd.DataFrame(data2)
print("DF2 with dic\n", df2)


df3 = pd.DataFrame(data2, index=['rank1','rank2','rank3','rank4'])
print("DF3 with custiom indexs on row is\n",df3)


#DataFrame from List of Dicts

data3 = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df4 = pd.DataFrame(data3, dtype= 'float64')
print("DF4 with list of dict\n", df4)

df5 = pd.DataFrame(data3, index=['first', 'second'], dtype="float64")
df5.columns = ["first_col", "secnd_col", "thrd_col"]
print("DF5 with list of dic with custom index\n", df5)

#DataFrame from Dict of Series

data4 = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c'], dtype="float64"),
         'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'], dtype="float64")}
df6 = pd.DataFrame(data4)
print("DF6 with list of Series\n", df6)
#Column Selection

data5 = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
         'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df7 = pd.DataFrame(data5)
print("Column values are\n", df7['one'])

"""
 
# Adding a new column to an existing DataFrame object with column label by passing new series

print ("Adding a new column by passing as Series:")
df7['three'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print("After adding new column\n", df7)

print ("Adding a new column using the existing columns in DataFrame:")
df7['four'] = df7['one'] + df7['three']
print("New df after adding is\n", df7)


#Row Selection, Addition

data6 = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
         'two' : pd.Series([1, 2, 30, 4], index=['a', 'b', 'c', 'd'])}

df8 = pd.DataFrame(data6)
print("DF8 with row selection is\n", df8.loc['b'])


#Selection by integer location
print("DF8 with row integer selection is\n", df8.iloc[2])

#Slice Rows

print("DF8 with slicing operator is\n", df8[2:4])

#Addition of Rows
df9 = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df10 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df9 = df9.append(df10)
print("DF9 after appending is\n", df9)

"""
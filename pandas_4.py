import numpy as np
import pandas as pd

# df_data = [['Henry',65],['Matt',45],['lynn',60]]
# df = pd.DataFrame(df_data,index=['R1','R2','R3'],columns=['name','marks'])

# df.sort_index()
# df.sort_index(ascending=True)
# print(df.sort_index(axis=1))#axis=0: Refers to the rows.axis=1: Refers to the columns.

# sample_obj =pd.Series(np.arange(2,10,2),index=['one','two','three','four'])
# print(sample_obj)
# print(sample_obj.sort_index())

# df['Age']=[23,18,22] #inserting age column
# df.loc['R4']=["mike",57,25] #iserting new r4 row

# print(df.sort_values(by='Age')) #sorting by age
# df.loc['R5'] = ['jake',60,27] 

# print(df.sort_values(by=['marks','Age'])) #priority for marks .if marks same then age consider

# print(df.loc[df["Age"]>18,['name','marks']])

# print(df.sort_values(by=['Age','marks'],ascending=False,kind='mergesort'))

#Concatenation of pandas objects
#just like conctenation of other python objcts like strings ,lists,tuple,etc
#useful in cases where you'll have to merge data from different sources or databases
#The functions provided ny panda for this purpose is the pd.concat() function
#you can concatenate objects in either row-wise or column-wise manner

#reindexing of Datframes ojects i pandas
#Reindexing gives you control over how your data aligns with the collections OverflowError#this is useful when you are working with data from different sources,alighning

#what is reindexing
#it is the technique which is used to conform your data to amtch a new set of labels along with your specified rows and columns
#reordering,insert missing values, fill missing values - in these scenarios, you
#reindex() and reindex_like(), you use this in combination with filling methods
s=pd.Series(np.random.rand(5),index=['a','b','c','d','e'])
print(s)

print(s.reindex((['e','b','f','d'])))
df_data = [["henry",67,"Aus"],["matt",54,"jpn"],['Lynn',60,"usa"]]
df = pd.DataFrame(df_data,columns=['Name','Age','Country'])

df.reindex(index=[1,2,3],columns=["Name","Country"])

#many a times you may need to reinedex one dataframe to alighn with another
#to perfrm this, you make use of the reindex_like() method

df1 =pd.DataFrame(np.random.randn(7,3),columns=["col1","col2","col3"])
df2 =pd.DataFrame(np.random.randn(2,3),columns=["col1","col2","col3"])

df1.reindex_like(df2)

print(df2.reindex_like(df1,method='ffill'))

#your method parameter can also be set to the value of nearest
df2.loc['4']=[np.nan,np.nan,np.nan]
df2.loc['5']=[np.nan,np.nan,np.nan]
df2.loc['6']=[np.nan,np.nan,np.nan]
df2.loc['7']=np.random.randn(3)
print(df2)
#print(df1.reindex_like(df2,method='nearest'))

#--------------------------------------------------------------------------------------
#handle duplicated data in you pandas objects(dupplicated data = rows which appears more than one inyour pandas)
#reasons
#two major methods which can be used to deal with duplicated dat in pandas, duplicated(), and drop_duplicates()
#duplicated() retuns a boolean value,indiacting whther there are duplcate rows
# df = pd.DataFrame({
#     'name':['rahul','raj','rahul'],
#     'DOB':['01 dec 2017','14 apr 2010','01 dec 2017']
#     })


# print(df.duplicated())
# result = df.duplicated(subset=['name','DOB'])
# print(result)
# #delete duplicate using drop_duplicate()
# print(df.drop_duplicates())
# print(df.drop_duplicates(subset=['DOB']))

#counting and retrieving unique elemets in your dataframe
#there are two widely used functions in this purpose.they are nunique()
#nunique(axis=0,dropna=True)

df = pd.DataFrame({'A':[4,5,6],'B':[5,6,2]})
print(df.nunique())

df['C'] =[7,np.nan,7]

df.nunique(dropna=False)#dropna consider null value as unique

#to count the unique value row-wise, you jsut axis=1
df.nunique(axis=1)
print(df)
#you can get the count of your uique values present in each column using the .value_counts() 
print(df['B'].value_counts())


#you can get thearray of unique values using the .unique( method, you can use )
df.loc[3] = [3,-1,0]
df.loc[4] = [9,10,np.nan]

result = pd.unique(df['A'])
print(result)
print(pd.unique(df.loc[2]))
#you can also check for the uniqueness of your row and column labels as it is not 
df6 = pd.DataFrame({'A':[0,1,2] ,'B':[4,1,1]},index=['a','a','b'])
#check if the row indices are unique in the following way
print(df6.index.is_unique)
print(df6.index.duplicated())
print(df6.loc[df6.index.duplicated()])

#.set_flags() will provide you the ability of rejecting duplicate labels
#pd.Series([0,1,2],index=list('abb').set_flags(allow_duplicate_labels=False))

try:
    df6.set_flags(allows_duplicate_labels=False)
except:
    print("your dataframe has duplicate labels")

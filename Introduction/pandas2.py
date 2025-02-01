import pandas as pd
import numpy as np
#empty series objevt
#s.name = "empty series object"
#you can create a series object in multiple ways using a numpy array, using a python
# numpy_obj =pd.Series(np.array([1,2,3,4]),dtype=np.float64,name="numpy series")
# print(numpy_obj)

# numpy_obj.index =["one","two","three","four"]

# print(numpy_obj)
# print(numpy_obj['three'])

# list_obj = pd.Series([1,2,3,4,5,6,7],name="list object")
# tuple_obj = pd.Series((1,2,3,4,5,6,7),name="tuple object")
# #set cannot be created here
# #set_obj = pd.Series({1,2,3,4,5,6,7},name="tuple object")

# dict_obj = pd.Series({"a":1,"b":2,"c":3},name = "dictionary object")#keys will be values

# single_value_object=pd.Series(7,index=np.arange(7),name="single value object")#output values will be 7 7's and indexes will be 0 to 6
# #rep_object =pd.Series(([1,2,3],index=np.arrange(9),name="rep object")) #length of values and indexes must be same .therefor ethis coe wont run

# dict_dat ={'a':0,'b':1,'c':2}
# s=pd.Series(dict_dat,index=['b','c','x','d'])# for b and c indexes will be 1,2 for x and d index is NaN

# #Slicing a series object
# #we have seen that series object are nothing but a non dimensional labelled array of elemnts
# #So slicing works similarly to any one dimensional numpy array,but here you can slice your series object using both position and labels
# series_obj = pd.Series(data=np.arange(10),name="series object")
# print(series_obj[0:5])#using index

# print(series_obj['a':'c'])#labels


# series_obj1 = pd.Series(np.arange(5),index=["zero","one","two","three","four"])
# print(series_obj1['zero':'two'])

# #pandas supports label based slicing and it is inclusive of both the strat and the stop lables in the cases of a series object.
# print(series_obj1['four':'one':-1]) #here when slicing, end is also included
# print(series_obj1.ndim) #gives dimension of array
# series_obj1.values([0,1,2,3,4])
# print(series_obj1.dtype)
# print(series_obj1.at['four'])

# series_obj1 = pd.Series(np.arange(5),index=['zero','one','two','three'])
# print(series_obj1.loc['three'])
# # .iat -> acesses a singl4e value using its corresponding integer position
# print(series_obj1.iat['one']) #only integer is allowed so it wont run
# print(series_obj1.iat[4])

# print(series_obj1.empty) #indicates whether yur series object is empty or not
# print(series_obj1.index)

# print(series_obj1.hasnans) #indicates whether my series object has NaN values
# print(series_obj1.is_monotonic_increasing) #check whether 
#with panda series objects you have to ability to perform arithmetic operations in a vectorized manner
#ie that you can perform these operation without looping through the elements in 
#perform tehse operations on single series abject as well as multi

# series_obj2 = pd.Series(np.arange(7))
# print(series_obj2 -2)
# print(series_obj2 //2)

# series_obj3 =pd.Series(np.arange(8),list('abcsefgh'),name='ops_demo')
# print(series_obj3)

# #arithmetic ops btw two series
# series1= pd.Series(np.arange(7),index=list('abcdefg'))
# series2 = pd.Series(np.arange(6),index=list('defghi'))
# print(series1+series2)#same indexes get added. otherss NaN
# print(series1.tolist())
# print(series1.to_frame())
# print(series1.to_string())

#python dataframes 
#dataframe is a 2d labelled data structure that is used for data manipulation
#it can store data of different types.every column holds value of a single dataype and you can have multiple columns with multiple data types
#each row is labbelled with a unique index value and each column has unique label
#can perform operations like filtering,sorting, merging,gouping and transforming

#size of your dataframe can change you can add rows columns, or delete rows 
#you can perform arithmetic operations on rows and columns

# df = pd.DataFrame([1,2,3,4,5])
# print(df.shape)

# nested_list = [['alex',10],['bob',12,56],['calerke',20]]
# df = pd.DataFrame(nested_list)
# print(df)
# df.index=['first','second','third']
# print(df)

# df1 = pd.DataFrame([['mumbai',1],['delhi',3,6,1],['bengluru',2,8],['kolkata',5],['chennai',1]])
# print(df1.shape)#(5,4) because 5 rows and 4 column

# #from a dictionary of ndarrays/lists
# dict_list ={'name':['Tom','jack','steve','rick'],'age':[28,34,56,42]} #must have same length.not assigh NaN.name and age are column names
# df3 =pd.DataFrame(dict_list)
# print(df3)
# #create dataframe from a list of dictionaries
# sample_dict=[{'a':1,'b':2},{'a':5,'b':10,'c':20},{'a':9,'x':24,'b':2}] #a,b,c,x becomes column names
# df4 =pd.DataFrame(sample_dict)
# print(df4)

# #creating a datframe from a dictinary of series objects
# d ={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=list('abcd'))}
# df5 =pd.DataFrame(d)
# print(df5)
f=pd.DataFrame({'name':['steve','lia','vin','katie'],'age':[32,28,45,38],'gender':['male','female','male','female'],'grade':[3.45,3.90,4,2.78]},index=['r1','r2','r3','r4'])
print(f)
# .iloc is used for slicng your dataframe basd on position(integer bsed inexing)
# .loc is used for slicing datframe based on labels(idex label or column labels)

print(f['name'])#get name column and values
#print(f.loc[['steve','katie'],['name','age']])
print(f.loc[['r1', 'r4'], ['name', 'age']])

#f.loc[['row1','row2']]

f[f['grade']>3.5]

f[f['grade']>3.5 & f['age']>35] #instaed of and & symbol is used

f[[False,False,True,True]]

f.loc[f["age"]>=35,['name','grade']]

f.loc[f['age']>=35,'grade']=4.5#modifying single columns

#filter and update multiple columns
condition =f['name'].str.startswith('S')
f.loc[condition,['age','grade']]=[35,2.25]
condition = f['country']=='UK' & f['age']>=35
f.loc[condition,['name','review']]

#Renaming columns and rows of your dataframe
f=f.rename(columns={'name':'namm','country':'nation'},index={'row1':'entry1','row2':'entry2'})

#adding new columns
f['sport']=['cricket','football','rowing','rugby','boxing']
#adding between columns
f.insert(4,'city',['melbourne','detroit','london','manhattan','boston','sydney'])

f = f.drop(columns='city')
f.replace({'sports':'cricket','city':'melbourne'},"Nil",inplace=True)#replace values with Nil.inplace true means modify original data is modified


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

series_obj2 = pd.Series(np.arange(7))
print(series_obj2 -2)
print(series_obj2 //2)

series_obj3 =pd.Series(np.arange(8),list('abcsefgh'),name='ops_demo')
print(series_obj3)

#arithmetic ops btw two series
series1= pd.Series(np.arange(7),index=list('abcdefg'))
series2 = pd.Series(np.arange(6),index=list('defghi'))
print(series1+series2)#same indexes get added. otherss NaN
print(series1.tolist())
print(series1.to_frame())




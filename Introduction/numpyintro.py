import numpy as np
import sys #to see memory used
#numpy is a python library for scietific computing
#difference between a python list and numpy array is that numpy array can contain values of same datatype
#Why numpy is preffered
#it is memory efficient. You can control the usage of memory through the available data types of numpy.it is devolped using C language
# it is capable of performing complex computations in an effiecient manner
x = [1,"Python",[1,2,3]] # python list

y=np.array([1,2,3,4])
print(type(y))
print(y.dtype)

#numpy arrays can only store values of a single type
y =np.append(y,"sample string")
y[0]+="string"
print(y)
xy_int = np.array([1,2,3,4],dtype=np.int32)#we can specify data type so it is memory efficient we can use int8,int 16,int32...
print(xy_int.dtype)

print(sys.getsizeof(xy_int))
#numpy support multidimensional array

xy_2d =np.array([[1,2,3],[4,5,6],[7,8,9]])
print(xy_2d[0,2])
print(xy_2d.shape)#show rows x col type
xy_b =np.array([[3,4,2],[6,7,3],[6,5,3]])
print(xy_2d + xy_b) #elemnt wise addition
print(xy_2d ** 0.5) #elemnt wise square root
print(xy_2d / xy_b) #element wise multiplication
print((xy_2d.T)) #transpose of array,not modify original array

xy_set =np.array({1,2,3})
print(xy_set.dtype) # here set is storing as object

xy_tuple =np.array((1,2,3))
print(xy_tuple.shape) #shape attribute returns tuple containing the values of each dimension

print(np.zeros((4,5))) #print zeroes for 4 rows & 5 columns.pass shape of array as tuple
#arrange method is similar to range method 
x= np.arange(9)
print(x) #output -> [0 1 2 3 4 5 6 7 8] return numpy array 

#linspace function--------------------------------------------------------
linspace_arr =np.linspace(4,5,9) #return an array of 9 elements which are evenly distributed between 4 and 5 including 4 and 5.start and end points are present in your array
#end-start /no of elemnts-1
print(linspace_arr)

x_arr =np.identity(5) #identity matrix with 5 rows

#reshape method-----------------------------------------------------------

re = x.reshape((3,3)) # x was [0 1 2 3 4 5 6 7 8]
print(re.sum(axis=0)) #axis=0 means along column sum,axis =1 means along row sum

#argmax(), argmin(), argsort()--------------------------------------------
d1 = np.array([8,2,4,1,6.1])
print(d1.argmax()) #return index of maximum value. which is 0 here
print(d1.argmin()) #return index of first occurence minimum value
print(d1.argsort()) #returns indexes of sorted elemnts (ie max lement index will be last)

sam =np.array([[1,2,3],[4,5,6]])
print(sam.argmax(axis=0)) #here returns 3 elemts which are indexes of max elemnts in each column

#ravel method
print(sam.ravel()) #2d array is conerted to 1d array

#matrix multiplication
a =np.array([[1,2,3],[4,5,6]])
b= np.array([[6,5,4],[3,2,1],[7,8,9]]) #no of columns of 1matrix must be equal to no of rows of 2nd
print(a@b)
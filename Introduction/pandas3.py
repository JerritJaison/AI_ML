import pandas as pd
import numpy as np
from io import StringIO
df=pd.DataFrame({'name':['steve','lia','vin','katie'],'age':[32,28,45,38],'gender':['male','female','male','female'],'grade':[3.45,3.90,4,2.78]},index=['r1','r2','r3','r4'])
print(df)
#you can delete 
print(df.drop(columns=['gender']))

df.insert(3,'Review',[3.75,4.25,4,4.78])
#i can pass the index value of row which need to be removed from your dataframe
print(df)

#df =df.drop('r3') #dropping r3
#print(df) #you can delete multiple rows from your df by a list of row labels to your drop() method
#df = df.drop()

print(df[df['Review']<=4])
df = df.drop(df.index[0::2])# get alternate rows using slicing
print(df)

df_num = pd.DataFrame(np.random.rand(4,5),index=['R1','R2','R3','R4'],columns=['C1','C2','C3','C4','C5']) #every elment is filled with random value
print(df_num+2)#2 is added 

#arithmetic opeation btw two dataFrames
#dataframes are alighned by thir index and column labels,so it will perform operations btw elemts of matching labels and returns Nan otherwise

df_num2 =pd.DataFrame(np.random.rand(3,3),index=['R3','R4','R5'],columns=['C1','C2','C3'])
print(df_num+df_num2) # 3 columns and two rows it will perform addtion .others are NaN

df3 =pd.DataFrame([['Python','High',1],['C++','low',2],['java','medium',3]],index=['R3','R4','R5'],columns=['C1','C2','C3'])
print(df3)

df_int = pd.DataFrame()

#pandas -I/O Tools
#we use read_csv in pandas for reading from csv files
#in your pd.read_csv function you have an argument term ehich is used to specify
#:, sep=':'
points_table = pd.read_csv(r'C:\Users\jerri\OneDrive\Documents\AI_ML\points_table.csv',dtype={'season':np.float32})#if we give names=['','ds'] it will give column nams as such
print(points_table)
#print(points_table.loc[points_table["season"]==2010],['name','against'])

# index_df =pd.read_csv("",header=None) #header none means the first entry is also treated as dat not heading
# index_df.columns=["slno",'name','level']

print(points_table.dtypes)
dict_of_types ={'season':np.float32}

#skiprows=2 means it skip 2 rows
dat_string ="""Name:Gender:age
Braun:male:22
Cumings:male:34
Katie:female:26
Catherine:female:28"""
#from io import StringIO then
obj1 =StringIO(dat_string) #converting string to object
df4 =pd.read_csv(obj1,sep=":")
print(df4)
df4.to_csv("sample.csv")#exporting to csv
table_df =pd.read_table(r'C:\Users\jerri\OneDrive\Documents\AI_ML\points_table.csv',sep=",")


data_json="""[
{"Name":"Braun","Gender":"Male","Age":30},             
{"Name":"Cumings","Gender":"Female","Age":20},
{"Name":"Kate","Gender":"Female","Age":28}]"""#objects are enclosed in {} in JSON
obj =StringIO(data_json)
df5=pd.read_json(obj)
#print(df5)

df6=pd.read_excel(r'C:\Users\jerri\OneDrive\Documents\AI_ML\sample_multi_sheet.xlsx')
#print(df6)

list1 = [[1,2010,"spain"],[2,2014,"germany"]]
df_list1 =pd.DataFrame(list1,index=["R1","R2"],columns=["s.no","year","country"])
df_list1.to_excel("football.xlsx",header=None,index=False)

list2= [[3,2018,"France"],[23,2015,"Argentina"]]
df_list2 =pd.DataFrame(list2,index=["R1","R2"],columns=["s.no","year","country"])

with pd.ExcelWriter("class_multisheet.xlsx") as xlwrite: #context manager
    df_list1.to_excel(xlwrite,sheet_name="first")
    df_list2.to_excel(xlwrite,sheet_name="second")

#appending list 3 to first sheet 
list3=[[4,2008,"Italy"],[13,2005,"Brazil"]]
df_list3 = pd.DataFrame(list3,index=['R3','R4'],columns=["s.no","year","country"])
with pd.ExcelWriter("class_multisheet.xlsx",mode='a') as xlwrite: #if mode is not used then the sheet will only have third sheet .first and second will be not there
    df_list3.to_excel(xlwrite,sheet_name="third")



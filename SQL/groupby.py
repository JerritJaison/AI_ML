import numpy as np
import pandas as pd

movies =pd.read_csv('imdb-top-1000.csv')
print(movies.head()) #head() print 5 rows t0 check data

#you only group your dataframe based on a categorical column
#it doesnt make sense to apply groupby on a numerical column
genres = movies.groupby('Genre') #will get dataframe returned

#you can apply aggregate functions on the groupby object to get results of every group which is present
print(genres.sum())

print(genres.max())#max in lexicographical order

print(genres['Series_Title'].max()) #this isnmore effiecient than print(genres.max(['Series_Title']))
#print(genres.max(['Series_Title']))

#fetch top three highest grossing genre
print(genres['Gross'].sum().sort_values(ascending=False).head(3))
#fetch top three genres with highest average rating
print(genres['IMDB_Rating'].mean().sort_values(ascending=False).head(3))
#find the name of director who is most popular
unique_director = movies.groupby('Director')

print(unique_director['No_of_Votes'].sum().sort_values(ascending=False))
print(unique_director['Series_Title'].count().sort_values(ascending=False).head(1))

#need to fetch the movies{and their rating} with highest imdb rating in each genre
print(movies.loc[genres['IMDB_Rating'].idxmax(),['Series_Title','Genre','IMDB_Rating']])#idxmax() gives index of higest value
#    --- or --- below code will print all movies if two or more movies has same rating
df = pd.DataFrame(columns=['Genre','Series_Title','IMDB_Rating']) #empty dataframe to hold the result
for name, group_df in genres:#iterating through each group like each genre .name will have each genre name
    max_rating = group_df['IMDB_Rating'].max()
    filtered_df = group_df[group_df['IMDB_Rating']==max_rating]
    df = pd.concat([df,filtered_df])
print(df[['Genre','Series_Title','IMDB_Rating']])

#important properties of groupby object----------------------
print(unique_director.groups) #movies dircted by who and their index in the dataset
#len(unique_director)

#for name,df in 

print(genres.first())#give first movie in the genre
print(genres.last())#returns last movie in the list

df =genres.nth(5)
print(df.shape)

#print name and count of movies in each genre that falls between each rating ranges

df_content=[]
for name, df2 in genres:#iterating through each group like each genre
    row_content =[] #used to store the value of each row
    row_content.append(name)
    for i in range(10):
        filtered_df = df2[df2['IMDB_Rating']>i]#filtered will ahev all movies which have rating greater tha i
        filtered_df =filtered_df[filtered_df['IMDB_Rating']<=i+1] #rating less than i+1 movies
        count_of_movies =filtered_df.shape[0]
        row_content.append(count_of_movies)
    df_content.append(row_content)
result_df = pd.DataFrame(df_content,columns=['Genre','0-1','1-2','2-3','3-4','4-5','5-6','6-7','7-8','8-9','9-10'])
print(result_df)


#print director and star which has movies fall between range 8-9 and 9-10    
directors = movies.groupby(['Director','Star1'])
df_contents=[]
for (director,star), df in directors:#iterating through each group like each genre
    row_content =[] #used to store the value of each row
    row_content.append(director)
    row_content.append(star)
    for i in range(8,10):
        filtered_df = df[df['IMDB_Rating']>i]#filtered will ahev all movies which have rating greater tha i
        filtered_df =filtered_df[filtered_df['IMDB_Rating']<=i+1] #rating less than i+1 movies
        count_of_movies =filtered_df.shape[0]
        row_content.append(count_of_movies)
    df_contents.append(row_content)
result_df = pd.DataFrame(df_contents,columns=['Director','Star','8-9','9-10'])
print(result_df)

#print genre and stars along with average imdb rating
df_list = [] #2d list to store row content
for name ,df in genres:
    inner_group =df.groupby('Star1')
    stars=[]
    max_rating=0
    row_content=[]
    row_content.append(name)
    for star_name,df1 in inner_group:
        avg_rating = df1['IMDB_Rating'].mean()
        if avg_rating > max_rating:
            stars.clear()
            stars.append(star_name)
            max_rating =avg_rating
        elif avg_rating ==max_rating:
            stars.append(star_name)
        else:
            continue
    row_content.append(max_rating)
    for sta in stars:
        row_content.append(sta)
        df_list.append(row_content.copy())
        row_content.pop()
result_df=pd.DataFrame(df_list,columns=['Genre','Avg_rating','star'])
print(result_df)


#display top 5 players who scored highest boundaries
cricket = pd.read_csv('deliveries.csv')
runs = cricket.groupby('batsman')
row_content=[]
for name,df3 in runs:
    filtered = df3[(df3['batsman_runs']==4) | (df3['batsman_runs']==6)]
    total_run= filtered['batsman_runs'].sum()
    row_content.append([name,total_run])
result_df =pd.DataFrame(row_content,columns=['Name','Total_boundary'])
#top_5 = result_df['Total_boundary'].sort_values(ascending=False).head(5)
result_df=result_df.sort_values(by='Total_boundary',ascending=False).head(5)
print(result_df)

#print the players who scored most in between 15th and 20th over
death_over=cricket[cricket['over'] >= 15].groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)
print(death_over)

matches = pd.read_csv('matches.csv')
season = matches.groupby('season')


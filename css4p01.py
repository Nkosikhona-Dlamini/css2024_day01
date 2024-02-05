# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 18:50:08 2024

@author: Nkosikhona Dlamini
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("movie_dataset.csv")
df.info()

"""
Checking for duplicates
"""
df.drop_duplicates(inplace = True)
print(df.shape)
#No duplicates found   
"""
Handling missing values in "Revenue (Mellions)" and "Metascore"
Deleting 
"""
df.dropna(inplace=True)
df.info()

"""
Checking for some strange values
"""
["Revenue (Millions)"]
       #.apply(lambda x: 
#True if r'D' in str else False )==True]
# Checking dataset 
pd.set_option('display.max_rows',None)
"""
highest rated movie
"""
y = df["Rating"].max()
highly_rated = df[df['Rating'] == 9.0]
print(highly_rated)
"""
Average Revenue (Millions)
"""
# Filter data for Revenue (class == 'Revenue')
Revenue_Ave = df['Revenue (Millions)'].mean()
#avg_Revenue = Revenue_Ave['Revenue (millions)'].mean()

"""
Average revenue of mivies from 2015 to 2017
"""
Average_Rev_2015_to_2017 = df[df['Year']>=2015]
AverageRevenue2015_2017= Average_Rev_2015_to_2017["Revenue (Millions)"].mean()

"""
Movies Released in 2016
"""
df_1 = pd.read_csv("movie_dataset.csv")
movies_2016 =df_1[df_1["Year"]==2016]
Number_of_Movies_in_2016 = len(movies_2016)

"""
Number of Movies were directed by Christopher Nolan
"""
y = df_1[df_1["Director"]== "Christopher Nolan"]
movies_directed_by_Nolan = len(y)

"""
Number of movies with a rating of at least 8.0
"""
z = df_1[df_1["Rating"]>=8.0]
movies_rating_atleast_8 = len(z)

"""
Median rating of movies directed by Christopher Nolan
"""
median_rating = y["Rating"].median()

"""
Year with the highest average rating
"""
years = ["year_2002","year_2003","year_2004","year_2005","year_2006","year_2007","year_2008","year_2009","year_2010","year_2011","year_2012","year_2013","year_2014","year_2015","year_2016","year_2017","year_2018","year_2019"]
year = [2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
add = 0
for i in range(0,16):
     years[i] = df_1[df_1["Year"]==year[i]]
     add = add + len(years[i])
#years[x] = df_1[y]["Rating"]==years[x]

for j in range(0,16):
    years[j] = years[j]['Rating'].mean()
    
"""
Percentage increase in number of movies made between 2006 and 2016
"""  
movies_2006 = df_1[df_1["Year"]== 2006]
movies_2016 = df_1[df_1["Year"]== 2016]

percentage_increase = 100*(len(movies_2016)-len(movies_2006))/len(movies_2006)
    
"""
most common actor in all the movies
"""
#actors = np.unique(np.hstack(df_1["Actors"].str.split(',')))
actors = np.hstack(df_1["Actors"].str.split(','))
n = len(actors)

maxcount = 0
freq_actor = 0 
for i in range(0,n):
        count = 0 
        for j in range(0,n):
            if (actors[i]== actors[j]):
                count += 1 
        if(count > maxcount):
            maxcount = count
            freq_actor = actors[i]
print(freq_actor)

"""
number of unique genres are there in the dataset
"""
n_genre = np.unique(np.hstack(df_1["Genre"].str.split(',')))
print(len(n_genre))

"""
correlation of the numerical features
We check to see if there were associations between the features and the Revenue made
1. Plot Revenue and Ratings
2. plot Revenue and Votes
3. plot Revenue and Metascore
4. plot heatmap correlation matrix

"""
plt.scatter(x=df["Rating"],y=df["Revenue (Millions)"])
plt.title("Rating vs. Revenue")
plt.xlabel("Rating")
plt.ylabel("Revenue")
plt.show()
  
plt.scatter(x=df["Votes"],y=df["Revenue (Millions)"])
plt.title("Votes vs. Revenue")
plt.xlabel("Votes")
plt.ylabel("Revenue")
plt.show()  

plt.scatter(x=df["Metascore"],y=df["Revenue (Millions)"])
plt.title("Metascore vs. Revenue")
plt.xlabel("Metascore")
plt.ylabel("Revenue")
plt.show()
   
numeric = df.drop(["Rank","Title","Genre","Description","Director","Actors"],axis=1)

correlation_matrix = numeric.corr(method="pearson")
sns.heatmap(correlation_matrix, annot=True)
plt.title("Correlation Matrix for Numerical feactures")
plt.xlabel("Numeric features")
plt.ylabel("Numeric features")
plt.show()
    
    












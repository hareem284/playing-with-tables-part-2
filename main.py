#Imagine that you are part of the Data Analytics team of the Mavericks Cricket Team. A database is provided to you that consists of all the details and statistics of the team. For analyzing the data of the Matches table, perform the following tasks of using SQL statements.

# importing sqlite3
import sqlite3
# importing pandas
import pandas as pd
connection=sqlite3.connect("database.sqlite")
print("connection is established congratulations")
# doing some stuff
read=pd.read_sql("SELECT Season_Id FROM Match",connection)
print(read.head())
# get the average win margain of all the winning teams for season 9
print(read.info())
reads9=pd.read_sql("SELECT AVG(Win_Margin),Match_Winner FROM Match WHERE Season_Id=9 GROUP BY Match_Winner",connection)
print(reads9)
#get the sum win margin of all the winning teams for season 9
readingsum=pd.read_sql("SELECT SUM(Win_Margin),Match_Winner FROM Match WHERE Season_Id =9",connection)
print(readingsum)
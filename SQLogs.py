#Initial import for necessary modules
import psycopg2

#Make method to parse raw data from SQL for question 1
def resParse1(list):
    ansList=[]
    for i in list:
        pass

#Connect to SQL database and create a cursor
db = psycopg2.connect(database="news")
c = db.cursor()

#Answer question 1
c.execute("select path, count(*) as num from log group by path
           order by num desc limit 3 offset 1;")
temp1=c.fetchall()
answer1=resParse1(temp1)

#Close connection
db.close()

#The output below will print answers to the questions using assigned variables
print("What are the most popular three articles of all time?")
#Insert answer1
print("Who are the most popular article authors of all time?")
#Insert answer2
print("On which days did more than 1% of requests lead to errors?")
#Insert answer 3
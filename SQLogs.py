#Initial import for necessary modules
import psycopg2

#Connect to SQL database and create a cursor
db = psycopg2.connect(database="news")
c = db.cursor()

#Answer question 1
c.execute("select title, count(*) as num from log join articles on substring(path, 10, length(path))=slug group by title order by num desc limit 3 offset 1;")
answer1=c.fetchall()

#Close connection
db.close()

#The output below will print answers to the questions
print("What are the most popular three articles of all time?\n")
for i in range(0, 3):
    print("#"+str(i+1)+" article name is "+answer1[i][0]+". It has been accessed "+str(answer1[i][1])+" times")
print("\n")
print("Who are the most popular article authors of all time?")
#Insert answer2
print("On which days did more than 1% of requests lead to errors?")
#Insert answer 3
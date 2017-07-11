# Python3
# Initial import for necessary modules
import psycopg2

# Connect to SQL database and create a cursor
db = psycopg2.connect(database="news")
c = db.cursor()

# Answer question 1
c.execute("select title, count(*) as num from log join articles on \
            substring(path, 10, length(path))=slug group by title \
            order by num desc limit 3 offset 1;")
answer1 = c.fetchall()

# Answer question 2
c.execute("select authors.name, count(*) as num from authors join \
            articles on authors.id=articles.author join log on \
            substring(path, 10, length(path))=slug group by \
            authors.name order by num desc;")
answer2 = c.fetchall()

# Close connection
db.close()

# The output below will print answers to the questions
print("What are the most popular three articles of all time?\n")
for i in range(0, 3):
    print("#"+str(i+1)+" article name is "+answer1[i][0]+". \
            It has been accessed "+str(answer1[i][1])+" times")
print("\n")

print("Who are the most popular article authors of all time?\n")
for i in range(0, len(answer2)):
    print("#"+str(i+1)+" author name is "+answer2[i][0]+". \
            This author has had "+str(answer2[i][1])+" views")
print("\n")

print("On which days did more than 1% of requests lead to errors?\n")
print("\n")
# Insert answer 3
# select extract(day from time) as date, count(*) as num from log
# where status!='200 OK' group by date order by date desc

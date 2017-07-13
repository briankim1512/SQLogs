#!/usr/bin/env python3
# Initial import for necessary modules
import psycopg2

# Connect to SQL database and create a cursor
db = psycopg2.connect(database="news")
c = db.cursor()

# Answer question 1
c.execute("select title, count(*) as num from log join articles on \
            substring(path, 10, length(path))=slug group by title \
            order by num desc limit 3;")
answer1 = c.fetchall()

# Answer question 2
c.execute("select authors.name, count(*) as num from authors join \
            articles on authors.id=articles.author join log on \
            substring(path, 10, length(path))=slug group by \
            authors.name order by num desc;")
answer2 = c.fetchall()

# Answer question 3
c.execute("select to_char(date, 'YYYY-MM-DD'), perc from (select \
            date_trunc('day', time) as date, round(count(case \
            status when '200 OK' then null else 1 end) * 100.0 / \
            (count(status)), 2) as perc from log group by date order \
            by date asc) as temp where perc > 1;")
answer3 = c.fetchall()

# Close connection
db.close()

# The output below will print answers to the questions
# Question 1
print("What are the most popular three articles of all time?\n")

for i in range(0, 3):
    print("#" + str(i+1) + " article name is " + answer1[i][0] + ". " +
          "It has been accessed "+str(answer1[i][1])+" times")
print("\n")

# Question 2
print("Who are the most popular article authors of all time?\n")

for i in range(0, len(answer2)):
    print("#" + str(i+1) + " author name is " + answer2[i][0] + ". " +
          "This author has had "+str(answer2[i][1])+" views")
print("\n")

# Question 3
print("On which days did more than 1% of requests lead to errors?\n")

for i in range(0, len(answer3)):
    print("On the date " + str(answer3[i][0]) + ", " + str(answer3[i][1]) +
          "% of the " + "requests lead to errors.")
print("\n")

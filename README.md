Prerequisites to running this file...
You must have python3, psycopg2, psql, and the news 
database within your system.
If not, follow these instructions:

To install Python, download the installer from here:
https://www.python.org/downloads/
and run the installer. Make sure it is Python 3 not Python 2

To get psycopg2, you must have had Python installed first.
Open CMD or a terminal with administrator rights and run the following command:
pip install psycopg2
This should automatically complete the install of psycopg2 to your system.

To get psql, follow the instructions given here:
http://postgresguide.com/setup/install.html

The news database is given by the admin of such database.
The original code was written from the database given by Udacity on:
2017-07-10
The news database may have changed from then. Regardless, the code will
(should) run without fault.


This program SQLogs will be able to find the following questions from the "news" database

1:What are the most popular three articles of all time?
2:Who are the most popular article authors of all time?
3:On which days did more than 1% of requests lead to errors?

The program will return these statements in a readable fashion for any viewer to understand regardless of prior programmingexperience or not.

To run the program, open the folder in terminal and run this command:
python3 SQLogs.py
The output should answer those aforementioned questions.
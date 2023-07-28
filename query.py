import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
# to Fetch Entire Table 
# mycursor.execute("select * from test1.test_table")

# To Fetch Particular Attibute
mycursor.execute("select c1,c5 from test1.test_table")

for i in mycursor.fetchall():
    print(i)

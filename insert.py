import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("insert into test1.test_table value(3424, 'anmol' ,234 ,345.56, 'rana')")
mycursor.execute("insert into test1.test_table value(3424, 'anmol' ,234 ,345.56, 'rana')")
mycursor.execute("insert into test1.test_table value(3424, 'anmol' ,234 ,345.56, 'rana')")
mycursor.execute("insert into test1.test_table value(3424, 'anmol' ,234 ,345.56, 'rana')")
mycursor.execute("insert into test1.test_table value(3424, 'anmol' ,234 ,345.56, 'rana')")
mydb.commit()
mydb.close()
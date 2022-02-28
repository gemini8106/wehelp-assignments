#使用connetion pool
from mysql.connector import pooling
connection_pool= pooling.MySQLConnectionPool(pool_name= "mydb_pool",
                                             pool_size= 5,
                                             pool_reset_session= True,
                                             host= "localhost",
                                             user= "root",
                                             password= "qwer1234",
                                             database= "website"
                                             )










#以下為不使用connetion pool的寫法(寫在主頁的py中)
#import mysql.connector以此與masql資料庫連結
# import mysql.connector
# mydb= mysql.connector.connect(
#   host= "localhost",
#   user= "root",
#   password= "qwer1234",
#   database= "website"
# )





from flask import Blueprint
app2= Blueprint("app2",__name__)
from flask import request, jsonify, redirect, session
from mysql.connector import pooling
connection_pool= pooling.MySQLConnectionPool(pool_name= "mydb_pool",
                                             pool_size= 5,
                                             pool_reset_session= True,
                                             host= "localhost",
                                             user= "root",
                                             password= "qwer1234",
                                             database= "website"
                                             )


#處理路徑(會員搜尋api)
@app2.route("/api/members", methods=["GET"])
def members():
  #由query string取得username
  username= request.args.get("username")
  
  mydb= connection_pool.get_connection()
  cursor= mydb.cursor()
  #取得指定username的資料
  cursor.execute("SELECT* FROM member WHERE username= %s",(username,) )
  user= cursor.fetchone()
  cursor.close()
  mydb.close()
  if user:
    #使用jsonify，將資料變成jason格式來傳輸，user[]表示fetchone後的第幾項資料
    return jsonify({"data":{"id":user[0], "name":user[1], "username":user[2]}})
  else:
    return jsonify({"data":None})
  
  
  
#處理路徑(更新姓名api)
@app2.route("/api/member", methods= ["POST"])
def changeName():
  #接收從js那傳輸過來的{"name":"_"}，並以get_json()改為dic
  newNameData= request.get_json()
  #取得dic中的"_"
  newName= newNameData["name"]
  #因為要修改name，所以以username來確認有沒有登入

  #如果輸入空值，直接導回原頁面
  if newName== "":
    return redirect("/member/")
  #如果有登入，使用資料庫update方法將新的名字更新進去
  elif "username" in session:
    
    mydb= connection_pool.get_connection()
    cursor= mydb.cursor()
    cursor.execute("""UPDATE member SET name= %s WHERE username= %s""", (newName,session["username"],))
    mydb.commit()
    cursor.close()
    mydb.close()
    #記得將新的name寫入session才會顯示在html頁
    session["name"]= newName
    
    return jsonify({"OK":True})
  
  else :
    return jsonify({"error":True})
  
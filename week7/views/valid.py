from flask import Blueprint
app3= Blueprint("app3", __name__)
from flask import request, redirect, render_template, session, url_for
from views.database import connection_pool



#處理路徑(註冊頁)，使用POST方法驗證(若沒有特別寫出來都適用GET方法)，POST方法安全性較高，若是帳密一定要用POST
@app3.route("/signup/", methods=["POST"])
def signUp(): 
  name= request.form["name"]
  username= request.form["username"]           #POST的取數值方法(request.form["account"](account為html input中輸入的值))
  password= request.form["password"]
  
  mydb= connection_pool.get_connection()
  cursor= mydb.cursor()
  #執行mysql資料庫選別，選出username重複的並fetch出來
  cursor.execute("SELECT * FROM member WHERE username= %s",(username,))      
  checkUsername= cursor.fetchone()
  
  #若註冊任一為空值，連到error頁顯示"請輸入完整資訊"
  if name== "" or username== "" or password== "":
    m= "請輸入完整資訊"
    return redirect(url_for("error", message= m))
  #若fetch到，則為true，代表資料庫中已有相同username，到error頁顯示"帳號已被註冊"
  if checkUsername :
    m= "帳號已經被註冊"
    return redirect(url_for("error", message= m))
  #若沒有fetch到，為false，則建立資料進資料庫，並導向註冊成功頁
  else:
    cursor.execute("INSERT INTO member(name, username, password) VALUES(%s, %s, %s)",(name, username, password,))
    #若資料庫有修改，一定要加上commit
    mydb.commit()
    cursor.close()
    mydb.close()
    return render_template("success.html")
  
  
  


#處理路徑(驗證頁)
@app3.route("/signin/", methods= ["POST"])
def signIn(): 
  username= request.form["username"]           #POST的取數值方法(request.form["account"](account為html input中輸入的值))
  password= request.form["password"]
  
  mydb= connection_pool.get_connection()
  cursor= mydb.cursor()
  #使用資料庫選別username和password都符合的會員資料，符合則fetch出來
  cursor.execute("SELECT * FROM member WHERE username= %s AND password= %s",(username, password,))
  checkUser= cursor.fetchone()
  #如果有fetch到為true，將name加入到session中，因為上面已有fetch到資料，所以直接使用checkUser變數，另外因其資料為tuple型態，故要加上索引[1]選取需要的name資料，並導向會員頁
  #除了name之外，另外再加入session["username"]，在(更新姓名api)會使用到
  cursor.close()
  mydb.close()
  if checkUser:
    session["name"]= checkUser[1]
    session["username"]= checkUser[2]
    return redirect("/member/")
  #若沒有fetch到資料，則導向error頁，顯示"帳號或密碼輸入錯誤"
  else:
    m= "帳號或密碼輸入錯誤"
    return redirect(url_for("error", message= m))







#在sign up頁及sign in頁中的％s也可改成%(username)s,{'username':username }
#cursor.execute("SELECT * FROM member WHERE username= %s",(username,)) = cursor.execute("SELECT * FROM member WHERE username= %(username)s",{'username':username})
#cursor.execute("SELECT * FROM member WHERE username= %s AND password= %s",(username, password,)) = cursor.execute("SELECT * FROM member WHERE username= %(username)s AND password= %(password)s",{'username':username, 'password':password})

#在sign up頁中
#cursor.execute("INSERT INTO member(name, username, password) VALUES(%s, %s, %s)",(name, username, password,)),
# 前面限制要insert的為name,username,password,就可以不用在後面把全部的數字寫出來
#若沒有打出來就要寫成cursor.execute("INSERT INTO member VALUES(default, %s, %s, %s, default, default)",(name, username, password,)),
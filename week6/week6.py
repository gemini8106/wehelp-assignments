from pickle import TRUE
from sqlite3 import Cursor
from flask import Flask  #載入Flask
from flask import request  #載入request物件
from flask import redirect #載入redirect函式
from flask import render_template  #載入render_template函式，記得建立templates資料夾
from flask import url_for   #載入url_for函式
from flask import session   #載入session物件

#import mysql.connector以此與masql資料庫連結
import mysql.connector
mydb= mysql.connector.connect(
  host= "localhost",
  user= "root",
  password= "qwer1234",
  database= "website"
)



#建立logIn物件
logIn = Flask(__name__,
  # 靜態處理，此處建立static資料夾用來放css，html檔才可使用
  static_folder="static",   #資料夾名static
  static_url_path="/static"   #資料夾路徑"/static"
              )
logIn.debug= True

#session的密鑰
logIn.secret_key= "hfewuiphfvbal"   

#處理路徑(登入頁)
@logIn.route("/")
def index():
  return render_template("index.html")  #route發送要求給後端，後端將index頁面給前端呈現   

#處理路徑(註冊頁)，使用POST方法驗證(若沒有特別寫出來都適用GET方法)，POST方法安全性較高，若是帳密一定要用POST
@logIn.route("/signup/", methods=["POST"])
def signUp(): 
  name= request.form["name"]
  username= request.form["username"]           #POST的取數值方法(request.form["account"](account為html input中輸入的值))
  password= request.form["password"]
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
    return render_template("success.html")
  
  


#處理路徑(驗證頁)
@logIn.route("/signin/", methods= ["POST"])
def signIn(): 
  username= request.form["username"]           #POST的取數值方法(request.form["account"](account為html input中輸入的值))
  password= request.form["password"]
  cursor= mydb.cursor()
  #使用資料庫選別username和password都符合的會員資料，符合則fetch出來
  cursor.execute("SELECT * FROM member WHERE username= %s AND password= %s",(username, password,))
  checkUser= cursor.fetchone()
  #如果有fetch到為true，將name加入到session中，因為上面已有fetch到資料，所以直接使用checkUser變數，另外因其資料為tuple型態，故要加上索引[1]選取需要的name資料，並導向會員頁
  if checkUser:
    session["name"]= checkUser[1]
    return redirect("/member/")
  #若沒有fetch到資料，則導向error頁，顯示"帳號或密碼輸入錯誤"
  else:
    m= "帳號或密碼輸入錯誤"
    return redirect(url_for("error", message= m))

 
  
  
#處理路徑(會員頁)
@logIn.route("/member/")
def member():
  # 如果輸入的name資訊還記錄在session內，直接導向會員頁(在導向時將username的值也傳遞過去，和url_for方式不同)
  if "name" in session:
    return render_template("member.html",name= session["name"])
  # 若session["name"]在sighout時刪除，重新導向首頁
  else:
    return redirect("/")



#處理路徑(錯誤頁)
@logIn.route("/error/")     
def error():
  #錯誤頁的網址中的query string，其message的資料由url_for取得
  result=request.args.get("message")
  #取得data給error.html網頁呈現錯誤訊息
  return render_template("error.html",data= result)    



#處理路徑(登出頁)
@logIn.route("/signout/")
def signout():
  session.pop("name",None)       #將session中的name資料刪除並重新導回首頁
  return redirect("/")


#處理路徑(返回首頁)
@logIn.route("/backhome/")
def backhome():
  return redirect("/")



logIn.run(port= 3000)                        #跑logIn物件，port為將網址埠號改為3000
mydb.colse()
from flask import Flask  #載入Flask
from flask import request  #載入request物件
from flask import redirect #載入redirect函式
from flask import render_template  #載入render_template函式，記得建立templates資料夾
from flask import url_for   #載入url_for函式
from flask import session   #載入session物件

#建立logIn物件
logIn = Flask(__name__,
  # 靜態處理，此處建立static資料夾用來放css，html檔才可使用
  static_folder="static",   #資料夾名static
  static_url_path="/static"   #資料夾路徑"/static"
              )

#session的密鑰
logIn.secret_key="hfewuiphfvbal"      


#處理路徑(登入頁)
@logIn.route("/")
def index():
  return render_template("index.html")  #route發送要求給後端，後端將index頁面給前端呈現

#處理路徑(驗證頁)，使用POST方法驗證(若沒有特別寫出來都適用GET方法)，POST方法安全性較高，若是帳密一定要用POST
@logIn.route("/signin/", methods=["POST"])
def signIn():                               #signIn函式
  account=request.form["account"]           #POST的取數值方法(request.form["account"](account為html input中輸入的值))
  code=request.form["code"]                 #POST的取數值方法(request.form["code"](code為html input中輸入的值))
  
  #若輸入的帳密和設定相符，呈現success.html頁面
  if account=="test"and code=="test":       
    session["account"]=account              #讓session記住輸入的帳戶名，可以在未登出的狀態下重新連結到會員頁
    return redirect("/member/")              #python的聯集用and，js使用&
  
  #任一為空白，顯示請輸入帳密
  elif account=="" or code=="": 
    m="請輸入帳號、密碼"
    return redirect(url_for("error",message=m))     #使用url_for取得message值，再連結到error頁面時可以呈現在query string
  
  #任ㄧ輸入錯誤，顯示帳密錯誤
  elif account!="test" or code!="test":
    m="帳號、或密碼錯誤"
    return redirect(url_for("error",message=m))
  
#處理路徑(會員頁)
@logIn.route("/member/")
def success():
  #如果輸入的accout資訊還記錄在session內，直接導向會員頁
  if "account" in session:
    return render_template("success.html")
  #若資訊在sighout時刪除，重新導向首頁
  else:
    return redirect("/")
  
#處理路徑(錯誤頁)
@logIn.route("/error/")     #錯誤頁的網址中的query string，其message的資料由驗證頁的url_for取得
def error():
  result=request.args.get("message")
  return render_template("error.html",data=result)    #取得data給error.html網頁呈現錯誤訊息

#處理路徑(登出頁)
@logIn.route("/signout/")
def signout():
  session.pop("account",None)       #將session中的account資料刪除並重新導回首頁
  return redirect("/")


logIn.run(port=3000)                        #跑logIn物件，port為將網址埠號改為3000

from flask import Flask, jsonify  #載入Flask
from flask import request  #載入request物件
from flask import redirect #載入redirect函式
from flask import render_template  #載入render_template函式，記得建立templates資料夾
from flask import url_for   #載入url_for函式
from flask import session   #載入session物件
from flask import Blueprint
from api.api import app2
from valid.valid import app3





#建立app物件
app = Flask(__name__,
  # 靜態處理，此處建立static資料夾用來放css，html檔才可使用
  static_folder="static",   #資料夾名static
  static_url_path="/static"   #資料夾路徑"/static"
              )
app.register_blueprint(app2)
app.register_blueprint(app3)

app.debug= True

#session的密鑰
app.secret_key= "hfewuiphfvbal"   



#處理路徑(登入頁)
@app.route("/")
def index():
  return render_template("index.html")  #route發送要求給後端，後端將index頁面給前端呈現   

  
#處理路徑(會員頁)
@app.route("/member/")
def member():
  # 如果輸入的name資訊還記錄在session內，直接導向會員頁(在導向時將username的值也傳遞過去，和url_for方式不同)
  if "name" in session:
    return render_template("member.html",name= session["name"])
  # 若session["name"]在sighout時刪除，重新導向首頁
  else:
    return redirect("/")
  

#處理路徑(錯誤頁)
@app.route("/error/")     
def error():
  #錯誤頁的網址中的query string，其message的資料由url_for取得
  result=request.args.get("message")
  #取得data給error.html網頁呈現錯誤訊息
  return render_template("error.html",data= result)    



#處理路徑(登出頁)
@app.route("/signout/")
def signout():
  session.pop("name",None)       #將session中的name資料刪除並重新導回首頁
  session.pop("username",None)
  return redirect("/")


#處理路徑(返回首頁)
@app.route("/backhome/")
def backhome():
  return redirect("/")



app.run(port= 3000)                        #跑app物件，port為將網址埠號改為3000






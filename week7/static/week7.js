let changeButton= document.getElementById("change");
let button= document.getElementById("search");

//要求二：fetch API,呈現找到的name
function findName(){
  //取得html輸入的username值，必須寫在function內，寫在全域會取不到值，一直呈現空白
  let input= document.getElementById("inputUsername");

  let searchName= input.value;
  
  let src= "http://127.0.0.1:3000/api/members?username="+searchName;
  
  fetch(src)
    //第一個response.json()會將fetch到的json值轉為js的object讓js讀取
    .then(response => response.json())
    //取得的object設定名稱為user
    .then(user => {
      //若從api那取得的response為{data:null}，將"查無此會員"以innerHTML方法加到html中呈現
      if (user.data== null){
        document.getElementById("answer").innerHTML= "查無此會員";
      }
      //若從api那取得的response為{data:{id:_, name:_, username:_}}，以物件取值方式取得會員資料利用innerHTML方法加到html中呈現
      else {
        document.getElementById("answer").innerHTML= user.data.name+ "("+ user.data.username+ ")";
        document.getElementById("inputUsername").value="";
      }
      //若使用下列appendchild方法，在呈現時會無限的把結果貼上，使用innerHTML方法較好
      // let Answer= user.data.name+ "("+ user.data.username+ ")";
      // let addAnswer= document.createTextNode(Answer);
      // document.getElementById("answer").appendChild(addAnswer);
      
    })
    
    .catch(error => console.log("Error:",error));
    
  }

button.addEventListener("click",findName);

//要求三




function changeName(){
  let src= "http://127.0.0.1:3000/api/member"
  //取得想要更改的新姓名
  let newName= document.getElementById("changeName");
  //fetch到api/member，使勇fetch的傳輸方法，將想要的數值傳送到api
  fetch(src,{
    method: "POST",
    headers: {"content-type": "application/json"},
    //將request body以JSON.stringify改成json格式傳輸{"name":"_"}
    body: JSON.stringify({
      name: newName.value
      })
    })
    //第一個response.json()會將fetch到的json值轉為js的object讓js讀取
    .then(response => response.json())
    //取得的object設定名稱為check
    .then(check =>{
      //如果取得的值為{OK:true}，使用innerHTML顯示"更新成功"到html頁
    if (check.OK== true){
      document.getElementById("result").innerHTML= "更新成功";
      document.getElementById("changeName").value= "";
      // let addSussess= document.createTextNode("更新成功");
      // document.getElementById("result").appendChild(addSussess);
    }
    else if (check.error== true){
      document.getElementById("result").innerHTML= "更新失敗";
    }
    })
    .catch(error => console.log("Error:",error));
}

changeButton.addEventListener("click",changeName);




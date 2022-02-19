let changeButton= document.getElementById("change");
let button= document.getElementById("search");

//要求二：fetch API,呈現找到的name
function findName(){
  let input= document.getElementById("inputUsername");

  let searchName= input.value;
  
  let src= "http://127.0.0.1:3000/api/members?username="+searchName;
  
  fetch(src)
    .then(response => response.json())
    .then(user => {
      if (user.data== null){
        document.getElementById("answer").innerHTML= "查無此會員";
      }
      else {
        document.getElementById("answer").innerHTML= user.data.name+ "("+ user.data.username+ ")";
      }
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
  let newName= document.getElementById("changeName");

  fetch(src,{
    method: "POST",
    headers: {"content-type": "application/json"},
    body: JSON.stringify({
      name: newName.value
      })
    })
  .then(response => response.json())
  .then(check =>{
    if (check.OK=true){
      document.getElementById("result").innerHTML= "更新成功"
      // let addSussess= document.createTextNode("更新成功");
      // document.getElementById("result").appendChild(addSussess);
    }
    else if (check.error=true){
      document.getElementById("result").innerHTML= "更新失敗"
    }
  })
  .catch(error => console.log("Error:",error));
}

changeButton.addEventListener("click",changeName);




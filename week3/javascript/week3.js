
let src =
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
fetch(src)
  .then(response => response.json())   //回傳json格式資料
  .then(data => {
    let source = data.result.results   //娶到資料中的results
      for(let i in source) {           //在資料內取for迴圈
        let link = "https" + source[i].file.split("https")[1];   
        let addImage = document.createElement("img");            //加入img的tag標籤
        addImage.className = "scenery";                          //將img的classname設為scenery
        addImage.src = link;                                     //將網址加入tag標籤中
        document.getElementsByClassName("pic")[i].appendChild(addImage);    //將設定好的img標籤透過appendchild加入classname為pic的標籤內,最重要的是[i],這樣img標籤才能依序加入pic標籤內
        
        let name = source[i].stitle;                             //設變數name取得資料內的title
        let addTitle = document.createElement("div");            //加入div的tag標籤
        addTitle.className = "caption";                          //將div的classname設為caption
        let messange = document.createTextNode(name);            //設立文字節點
        addTitle.appendChild(messange);                          //將文字加入到<div></div>內
        document.getElementsByClassName("pic")[i].appendChild(addTitle);     //將設定好的div標籤透過appendchild加入classname為pic的標籤內,最重要的是[i],這樣div標籤才能依序加入pic標籤內
        }
    })  
   .catch(error => console.log("Error:",error))

//fetch格式
//fetch()
// .then(函式)
// .then(可以一直接.then)
//.catch(error => console.log("Error:",error))



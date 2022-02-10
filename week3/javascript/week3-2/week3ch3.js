
let src =
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
fetch(src)
  .then(response => response.json())
  .then(data => {
    let source = data.result.results
      for(let i in source) {
        let addBox = document.createElement("div");
        addBox.className = "pic";
        document.getElementsByClassName("container")[0].appendChild(addBox);    //countainer只有一個，必須寫[0]才會有答案出來
        

        let link = "https" + source[i].file.split("https")[1];
        let addImage = document.createElement("img");
        addImage.className = "scenery";
        addImage.src = link;
        document.getElementsByClassName("pic")[i].appendChild(addImage);    
        
        let name = source[i].stitle;
        let addTitle = document.createElement("div");
        addTitle.className = "caption";
        let messange = document.createTextNode(name);
        addTitle.appendChild(messange);
        document.getElementsByClassName("pic")[i].appendChild(addTitle);
        }
    })  
   .catch(error => console.log("Error:",error))



  
   

let loadmore = document.getElementById('loadmore');
  let currentPics = 8;
    loadmore.addEventListener("click",() => {
      let allPics = document.querySelectorAll('.container .pic');
      for (let i = currentPics; i < currentPics + 8; i++){
          allPics[i].style.display = 'block';
        }
      currentPics += 8;
    })





let src =
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
fetch(src)
  .then(response => response.json())
  .then(data => {
    let source = data.result.results
      for(let i in source) {
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


      
    //   
    //   // create title
    //   for (let y = 0 ; y <= listName.length ;y++){
    //     
    // //   }
    // // })
    // .catch(error => console.log("Error:",error))





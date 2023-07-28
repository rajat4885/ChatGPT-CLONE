
async function postData(url = "", data = {}) {
   
    const response = await fetch(url, {
      method: "POST",      
      headers: {
        "Content-Type": "application/json",
          },
      body: JSON.stringify(data), 
    }); 
    return response.json(); //return the post data to the flask server
  }
  

  

sendbutton.addEventListener("click",async()=>{
 questioninput= document.getElementById("questioninput").value; //getting the value from search bar to var question
 document.getElementById("questioninput").value="";
 document.querySelector(".right2").style.display="block"//when we click on submit button we display tha right 2 class ans hide the right 1 class
 document.querySelector(".right1").style.display="none"
 question.innerHTML= questioninput; //giving intput of search bar to our question 

 let result= await postData("/api",{"question":questioninput})
 solution.innerHTML=result.answer
 //sending the post request to server[main.py] and the request contains the text of search bar in json format
})
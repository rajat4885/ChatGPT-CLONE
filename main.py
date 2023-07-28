from flask import Flask,render_template,jsonify,request
from flask_pymongo import PyMongo


#---------------------------OPEN AI -----------------------------------------

import openai
openai.api_key = "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"

#-----------------------------MONGO DB-FLask----------------------------------
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/ChatGPT"
mongo = PyMongo(app)

@app.route("/")
def home():
    
    chats = mongo.db.chats.find({})
    myChats= [chat for chat in chats]
    return render_template("index.html",myChats=myChats)

@app.route("/api",methods=["GET","POST"]) #calling the post api
def qa():
    if request.method=="POST":
        print(request.json)#Print the question entered into terminal
        question= request.json.get("question") #creating var which get the data of incoming post request
        chat= mongo.db.chats.find_one({"question": question}) #used to check if the asked question is in our database already or not if present then return answer stored
        
        if chat:
            data={"question": question,"answer": f"{chat['answer']}"}
            return jsonify(data)
        else : #getting response from open AI
          response = openai.Completion.create( 
            model="text-davinci-003",
            prompt=question,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
                      )
          data={"question": question, "answer": response["choices"][0]["text"]} #will store data from open AI key 
          mongo.db.chats.insert_one({"question": question, "answer": response["choices"][0]["text"]})
          return jsonify(data) #return the answer in json format fron open AI key
    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss? "}
    return jsonify(data)  
    
app.run(debug= True)
import pickle
from flask import Flask,jsonify,request,app,render_template,url_for
import numpy as np
import pandas as pd
import spacy
app=Flask(__name__)
nlp=spacy.load('en_core_web_sm')
model=pickle.load(open("model.pkl","rb"))
@app.route('/')
def home():
    return render_template("Home.html")
@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method=="POST":
        data=request.form.get("inputText")
        data=nlp(data).vector
        final_data=np.array(data).reshape(1,-1)
        output=model.predict(final_data)
        if output == 0:
            prediction = "Fake"
        else:
            prediction = "Real"
        return render_template("Home.html", prediction="The prediction is: {}".format(prediction))
    else:
        return jsonify({"Invalid":"Invalid Request method"})
if __name__=="__main__":
    app.run(debug=True)
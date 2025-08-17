from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# this will creae an instance of a flask framework which will be our wsgi application
application=Flask(__name__)
app=application

ridge_model=pickle.load(open('model/ridge.pkl','rb'))
standard_scaler=pickle.load(open('model/scaler.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_data():

    if request.method=='POST':
        Temperature = float(request.form['Temperature'])
        RH = float(request.form['RH'])
        Ws = float(request.form['Ws'])
        Rain = float(request.form['Rain'])
        FFMC = float(request.form['FFMC'])
        DMC = float(request.form['DMC'])
        ISI = float(request.form['ISI'])
        Classes = float(request.form['Classes'])
        Region = float(request.form['Region'])

        scaled_data=standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        result=ridge_model.predict(scaled_data)

        return render_template('home.html',results=result[0])
    

    else:
        return render_template('home.html')
if __name__=="__main__":
    app.run(debug=True)
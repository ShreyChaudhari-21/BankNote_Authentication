# -*- coding: utf-8 -*-
"""
Created on Mon May 24 15:03:29 2021

@author: LENOVO PC
"""

import pandas as pd
import numpy as np
import pickle
from flask import Flask,request


app=Flask(__name__)
pickle_in=open('RFC.pkl','rb')
RFC=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Hello Welcome All "

@app.route('/predict',methods=["GET"])
def predict_Bank_Note():
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=RFC.predict([[variance,skewness,curtosis,entropy]])
    return "The Predicted Value is" + str(prediction)



if __name__ == '__main__':
    app.run()
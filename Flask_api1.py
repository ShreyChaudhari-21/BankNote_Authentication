# -*- coding: utf-8 -*-
"""
Created on Mon May 24 15:57:00 2021

@author: LENOVO PC
"""

import pandas as pd
import numpy as np
import pickle
from flask import Flask,request
import flasgger
from flasgger import Swagger


app=Flask(__name__)
Swagger(app)
pickle_in=open('RFC.pkl','rb')
RFC=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Hello Welcome All "

@app.route('/predict',methods=["GET"])
def predict_Bank_Note():
    """Let's Authenticate Banks Note .
    This is using docstring for specifications .
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The Output Values

    """
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=RFC.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)  
    return "Hello , The Predicted Answer is" + str(prediction)





if __name__ == '__main__':
    app.run()
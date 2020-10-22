import numpy as np
from flask import Flask, redirect, url_for, jsonify, render_template, url_for, request
import pickle


# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func





#################################################
# Flask Setup
#################################################
app = Flask(__name__)
# app = Flask(__name__, static_url_path='')


#################################################
# Flask Routes
#################################################



@app.route('/')
def root():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about_the_data')
def about_the_data():
    return render_template('about_the_data.html')

@app.route('/symptom_checker')
def symptom_checker():
    return render_template('symptom_checker.html')

@app.route('/graphs')
def graphs():
    return render_template('graphs.html')

@app.route('/results', methods=['POST'])
# def results():
    # # age = request.form.get('Age')
    # polyuria = 1 if request.form.get('Polyuria') is not None else 0

    # input_data = [[20,polyuria,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    
    # print(polyuria)
    # return str(polyuria)
    # if positive
    # return render_template('predicted_positive.html')
    # if negative
    # return render_template('predicted_negative.html')
@app.route('/action_page', methods=["post"])
def action_page():
    print(request.form)
    inputs=[]
    Age=float(request.form['Age'])
    inputs.append(Age)
    print(Age)
    try:
        Gender=float(request.form['Gender'])
        print(Gender)
    except:
        Gender=0
    inputs.append(Gender)
    try:
        Polyuria=float(request.form['Polyuria'])
        print(Polyuria)
    except:
        Polyuria=0
    inputs.append(Polyuria)
    try:
        Polydipsia=float(request.form['Polydipsia'])
        print(Polydipsia)
    except:
        Polydipsia=0
    inputs.append(Polydipsia)
    try:
        weight_loss=float(request.form['weight loss'])
        print(weight_loss)
    except:
        weight_loss=0
    inputs.append(weight_loss)
    try:
        weakness=float(request.form['weakness'])
        print(weakness)
    except:
        weakness=0
    inputs.append(weakness)
    try:
        Polyphagia=float(request.form['Polyphagia'])
        print(Polyphagia)
    except:
        Polyphagia=0
    inputs.append(Polyphagia)
    try:
        Genital_thrush=float(request.form['Genital thrush'])
        print(Genital_thrush)
    except:
        Genital_thrush=0
    inputs.append(Genital_thrush)
    try:
        visual_blurring=float(request.form['visual blurring'])
        print(visual_blurring)
    except:
        visual_blurring=0
    inputs.append(visual_blurring)
    try:
        Itching=float(request.form['Itching'])
        print(Itching)
    except:
        Itching=0
    inputs.append(Itching)
    try:
        Irritability=float(request.form['Irritability'])
        print(Irritability)
    except:
        Irritability=0
    inputs.append(Irritability)
    try:
        delayed_healing=float(request.form['delayed healing'])
        print(delayed_healing)
    except:
        delayed_healing=0
    inputs.append(delayed_healing)
    try:
        partial_paresis=float(request.form['partial paresis'])
        print(partial_paresis)
    except:
        partial_paresis=0
    inputs.append(partial_paresis)
    try:
        muscle_stiffness=float(request.form['muscle stiffness'])
        print(muscle_stiffness)
    except:
        muscle_stiffness=0
    inputs.append(muscle_stiffness)
    try:
        Alopecia=float(request.form['Alopecia'])
        print(Alopecia)
    except:
        Alopecia=0
    inputs.append(Alopecia)
    try:
        Obesity=float(request.form['Obesity'])
        print(Obesity)
    except:
        Obesity=0
    inputs.append(Obesity)
    print(inputs)
    model=pickle.load(open('./static/rfc.sav', 'rb'))
    
    prediction=model.predict([inputs])
    print(prediction)
    if prediction[0] == 0 :
        outcome='Negative'
    else:
        outcome='Positive'
    
    return render_template('symptom_checker.html', outcome=outcome)

# @app.route('/predicted_positive')
# def predicted_positive():
#     return render_template('predicted_positive.html')

# @app.route('/predicted_negative')
# def predicted_negative():
#     return render_template('predicted_negative.html')

if __name__ == '__main__':
    app.run(debug=True)

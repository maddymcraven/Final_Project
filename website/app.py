import numpy as np
from flask import Flask, redirect, url_for, jsonify, render_template, url_for, request

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


@app.route('/about_the_data')
def about_the_data():
    return render_template('about_the_data.html')

if __name__ == '__main__':
    app.run(debug=True)

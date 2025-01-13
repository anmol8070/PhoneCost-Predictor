from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
import os
from sklearn.metrics.pairwise import euclidean_distances, distance_metrics

model_file_path = 'C:/Users/Anmol/Downloads/Mobile price classification/Mobile price classification/model.pkl'

if not os.path.exists(model_file_path):
    print(f"Error: Model file '{model_file_path}' not found.")
    exit()

with open(model_file_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/home', methods=['POST','GET'])
def home():
    int_f = [float(x) for x in request.form.values()]
    final = [np.array(int_f)]
    prediction = model.predict(final)
    output = prediction[0]
    color = "black"
    if output == 0:
        color = "black"
        output_text = "Mobile is classified into low price range"
    elif output == 1:
        color = "black"
        output_text = "Mobile is classified into medium price range"
    elif output == 2:
        color = "black"
        output_text = "Mobile is classified into high price range"
    else:
        color = "black"
        output_text = "Mobile is classified into very high price range"
    return render_template('index.html', pred=output_text, color=color)

if __name__ == "__main__":
    print("Starting Python Flask Server For Mobile Price Classification...")
    app.run(debug=True)

from flask import Flask, render_template, request

import pickle
import numpy as np


model = pickle.load(open("model.pkl", 'rb'))
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    print(request.method)
    col = ['Furnished', 'Unfurnished', 'Semi-Furnished', 'Kolkata', 'Delhi',
           'Hyderabad', 'Bangalore', 'Chennai', 'Mumbai', 'min_floor', 'max_floor',
           'BHK', 'Size', 'Bathroom']
    if request.method == 'POST':
        BHK=int(request.form['bhk'])
        min_floor=int(request.form['min_floor'])
        max_floor=int(request.form['max_floor'])
        Size=float(request.form['size'])
        Bathroom=int(request.form['bathrooms'])
        furnish=request.form['Furnishing_Status']
        city=request.form['city']
        X = np.zeros(len(col))
        for i in range(len(col)):
            if(furnish==col[i]):
                X[i]=1
            if(city==col[i]):
                X[i]=1

        X[9]=min_floor
        X[10] = max_floor
        X[11] = BHK
        X[12] = Size
        X[13]= Bathroom

        y_predictions=np.round(model.predict([X])[0],2)
        print(y_predictions)
        return render_template('main.html', ypre=y_predictions)


if __name__ == "__main__":
    app.run()















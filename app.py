from flask import Flask, render_template, request

import pickle
import numpy as np

filename = 'diabetic.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        print(request.form)
        data1 = int(request.form['Pregnancies'])
        data2 = int(request.form['Glucose'])
        data3 = int(request.form['BloodPressure'])
        data4 = int(request.form['SkinThickness'])
        data5 = int(request.form['Insulin'])
        data6 = float(request.form['BMI'])
        data7 = float(request.form['DiabetesPedigreeFunction'])
        data8 = int(request.form['Age'])
        arr = np.array([[data1, data2, data3, data4,data5, data6, data7, data8]])
        pred = model.predict(arr)
        return render_template('result.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)
















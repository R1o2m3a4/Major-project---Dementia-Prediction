from flask import Flask, render_template,request, redirect, flash, session
from joblib import load
import pandas as pd
model = load('dementia_ai.jb')

app = Flask(__name__)
app.secret_key = "daosijalksd"

@app.route('/')
def home():
    return render_template('form.html')
@app.route('/predict',methods=['POST'])
def predict():
    try:
        age = int(request.form['age'])
        gender= request.form['Gender']
        educ = int(request.form['educ'])
        ses = float(request.form['ses'])
        mmse = float(request.form['mmse'])
        cdr = float(request.form['cdr'])
        inpdf = pd.DataFrame([{'M/F': gender, 'Age': age, 'EDUC': educ, 'SES': ses, 'MMSE': mmse, 'CDR': cdr}])
        prediction = model.predict(inpdf)
        return render_template('form.html', prediction=prediction[0])
    except Exception as e:
       flash('fill all fields correctly', 'danger')
       return redirect('/')
    


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
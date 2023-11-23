from flask import Flask,render_template,request
import pickle
import numpy as np


model = pickle.load(open('/Users/bakudi/Vaidik/Projects/Sales Predictions/model.pkl','rb'))

app = Flask(__name__)

@app.route ('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_sales():
    
    TV = float(request.form.get('TV'))
    Radio = float(request.form.get('Radio'))
    Newspaper = float(request.form.get('Newspaper'))
    
    sales = model.predict(np.array([TV,Radio,Newspaper]).reshape(1,3))
    
    sale = '$ ' + str(round(sales[0],2))
    return render_template('index.html',result=sale)
    
if __name__ == '__main__':
    app.run(debug=True)

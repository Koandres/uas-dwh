from run import app
from flask import render_template
from flask import request
from app.Controllers import predictController

@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'GET'):
        return render_template('index.html')


@app.route('/prediksi', methods=['POST'])
def predict():
    if (request.method == 'POST'):
        return predictController.getPredictSalesInYear()

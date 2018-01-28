from flask import Flask

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():


@app.route('/retrain', method=['POST'])
def retrain():
    

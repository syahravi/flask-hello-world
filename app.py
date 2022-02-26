from flask import Flask

app = Flask(__name__)

@app.route('/')
def apapunoke():
    return 'APA PUN OKE!'

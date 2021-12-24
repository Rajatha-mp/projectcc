import logging
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Cloud activity\n Team: Rajatha- 4MC18CS102\n Rashmi Basrur- 4MC18CS105\n'


if __name__== '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

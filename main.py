import logging
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Google App Engine (often referred to as GAE or simply App Engine) is a cloud computing platform as a service for developing and hosting web applications in Google-managed data centers. Applications are sandboxed and run across multiple servers'


if __name__== '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

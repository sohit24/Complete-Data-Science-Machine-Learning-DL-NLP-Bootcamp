from flask import Flask

## created an instance of flask which acts as WSGI
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the web"

@app.route('/index')
def index():
    return "This is the only index page"

if __name__ == '__main__':
    app.run(debug = True)
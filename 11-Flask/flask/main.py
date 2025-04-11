from flask import Flask, render_template

# instance
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello all'

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
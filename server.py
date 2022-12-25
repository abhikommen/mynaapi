from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello APi"

@app.route('/endpoint')
def endpoint():
    return "This is an end point. You can call send or receive requests by calling this end point."

@app.route('/linker')
def linker():
    return render_template('link.html')


app.run(debug = True, host="0.0.0.0",port=5555)
    #app.run(debug=True) #can alter host and port number here. Right now the default host is localhost and port is 5000
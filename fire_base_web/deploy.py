from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')



@app.route("/gauge")
def gauge():
    return render_template('gauge.html')


    
if __name__ == '__main__':
    app.run(debug=True)



@app.route('/public')
def public():
    return

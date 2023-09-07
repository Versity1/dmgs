from flask import Flask, render_template, url_for, request
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.secret_key = b'_53oi3uriq9pifpff;apl'
csrf = CSRFProtect(app)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/table")
def table():
    return render_template('table.html')

@app.route("/dream", methods=['POST', 'GET'])
def dream():
    if request.method == 'POST':
        name = request.form['Name']
        return (' Hello ' + name + '!!!')
    return render_template('dream.html')

if __name__ == "__main__":
    app.run(debug=True)
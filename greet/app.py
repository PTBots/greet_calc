from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    html = """
    <html>
        <body>
        <h1> Home Page </h1>
        <p>Welcome to my greeting app!</p>
        </body>
    </html>
    """

@app.route('/welcome')
def say_welcome():
    return "welcome"

@app.route('/welcome/back')
def say_welcome_back():
    return "welcome back"

@app.route('/welcome/home')
def say_welcome_home():
    return "welcome home"
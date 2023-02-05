from flask import Flask

# create an instance of a Flask web application
app = Flask(__name__)

# create a page that will be on the website. create a function. Inside the function, you can return an inline HTML.
@app.route("/")
def home():
    return "Hello! This is the main page <h1>HELLO<h1>"


if __name__ == "__main__":
    app.run()

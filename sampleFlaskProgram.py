from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World! This is Bharathwaj from Team Argus"


if __name__=="__main__":
    app.run() 
from flask import Flask,send_file

app = Flask(__name__)

@app.route("/")

def home():
    return send_file("index.html");

@app.route("/jquery.js")

def throw():
    return send_file("jquery.js")

@app.route("/<user>/<password>")
def check(user,password):
    if user == "Hacker" and password == "1514":
        return "True Credites !"
    return "False Credites !"

if __name__ == "__main__":
    app.run(debug=True,port="1514",host="0.0.0.0")

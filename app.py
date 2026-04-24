from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from CI/CD Pipeline!   Sap =500123228"

app.run(host="0.0.0.0", port=80)
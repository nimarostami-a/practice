from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "helloooo nima"

    

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Docker TEST TEST2 TEST3"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 4000)

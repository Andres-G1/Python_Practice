#Day-16 on python
''' Hi :), this is Day-16 in Python.
Congratulations for reaching Day-16.
In this day you are learning about libraries and Flask.
'''

# Libraries and Flask
# What is Flask?
''' Flask is a microframework in Python for building web applications.
It allows you to define routes, handle requests, and return responses.
'''

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Flask on Day-16!"


@app.route("/api/message")
def api_message():
    return jsonify({"message": "This is a JSON endpoint with Flask."})


@app.route("/api/sum")
def api_sum():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify({"result": a + b})
    except ValueError:
        return jsonify({"error": "Parameters must be integers."}), 400


if __name__ == "__main__":
    print("Make sure Flask is installed: pip install flask")
    app.run(debug=True)

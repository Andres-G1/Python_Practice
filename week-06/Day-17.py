#Day-17 on python
''' Hi :), this is Day-17 in Python.
Congratulations for reaching Day-17.
In this day you are learning more about Flask and dynamic routes.
'''

from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)


@app.route("/hello/<name>")
def hello(name):
    return render_template_string(
        "<h1>Hello, {{ name }}!</h1><p>This is a dynamic Flask route.</p>",
        name=name,
    )


@app.route("/api/product", methods=["POST"])
def api_product():
    data = request.get_json() or {}
    name = data.get("name")
    price = data.get("price")

    if not name or price is None:
        return jsonify({"error": "You must send name and price in JSON."}), 400

    return jsonify({"message": f"Product {name} received.", "price": price})


@app.route("/api/items")
def api_items():
    items = [
        {"id": 1, "name": "Book", "price": 25000},
        {"id": 2, "name": "Notebook", "price": 15000},
    ]
    return jsonify(items)


# ---- EXERCISES ----
'''
- Create a dynamic route that receives a name.
- Create a POST endpoint that receives JSON and returns a JSON response.
- Test these routes with the browser or a tool like Postman.
'''

if __name__ == "__main__":
    print("Make sure Flask is installed: pip install flask")
    app.run(debug=True)

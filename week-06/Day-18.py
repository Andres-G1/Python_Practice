#Day-18 on python
''' Hi :), this is Day-18 in Python.
Congratulations for reaching Day-18.
In this day you are completing a Flask project.
'''

# Project: mini Flask application
# This project is an example of a web application using Flask.

from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 150000},
    {"id": 2, "name": "Mouse", "price": 25000},
]


@app.route("/")
def index():
    html = """
    <h1>Product Catalog</h1>
    <ul>
    {% for product in products %}
      <li>{{ product.name }} - ${{ product.price }}</li>
    {% endfor %}
    </ul>
    <p>Use /api/products to see the products in JSON.</p>
    """
    return render_template_string(html, products=products)


@app.route("/api/products")
def api_products():
    return jsonify(products)


@app.route("/api/products", methods=["POST"])
def add_product():
    data = request.get_json() or {}
    name = data.get("name")
    price = data.get("price")

    if not name or price is None:
        return jsonify({"error": "name and price are required"}), 400

    next_id = max([p["id"] for p in products]) + 1 if products else 1
    product = {"id": next_id, "name": name, "price": price}
    products.append(product)
    return jsonify(product), 201


if __name__ == "__main__":
    print("Make sure Flask is installed: pip install flask")
    app.run(debug=True)

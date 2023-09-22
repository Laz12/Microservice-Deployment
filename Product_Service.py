from flask import Flask, jsonify, request

app = Flask(__name__)

# List of grocery items
products = [
    {"id": 1, "name": "Apples", "price": 2.0, "quantity": 100},
    {"id": 2, "name": "Bananas", "price": 1.0, "quantity": 50},
    {"id": 3, "name": "Mangoes", "price": 3.0, "quantity": 80},
]

# Endpoint 1: Retrieve list of grocery products, including their names, prices, and quantity in stock
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"products": products})


# Endpoint 2: Get details about a specific product by its unique ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404


# Endpoint 3: Adding new grocery products to the inventory
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if 'name' in data and 'price' in data and 'quantity' in data:
        product = {
            "id": len(products) + 1,
            "name": data['name'],
            "price": data['price'],
            "quantity": data['quantity']
        }
        products.append(product)
        return jsonify(product), 201
    return jsonify({"error": "Invalid product data"}), 400

@app.route('/products/update_quantity/<int:product_id>', methods=['PATCH'])
def update_product_quantity(product_id):
    data = request.get_json()
    quantity_change = data.get('quantity_change', 0)

    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        # Ensure that the quantity change doesn't result in a negative quantity
        if product['quantity'] + quantity_change >= 0:
            product['quantity'] += quantity_change
            return jsonify({"message": "Product quantity updated successfully"}), 200
        else:
            return jsonify({"error": "Quantity change would result in a negative quantity"}), 400
    return jsonify({"error": "Product not found"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)

from flask import Flask, jsonify, request

app = Flask(__name__)

# List of groceries
grocery_products = [
    {"id": 1,"name": "Apple", "price": 1.0, "quantity": 100},
    {"id": 2,"name": "Banana", "price": 0.5, "quantity": 150},
    {"id": 3,"name": "Carrot", "price": 0.75, "quantity": 75},
]



# Endpoint 1: Retrieve list of grocery products, including their names, prices, and quantity in stock
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"products": grocery_products})

# Endpoint 2: Get details about a specific product by its unique ID
@app.route('/products/<int:product_id>', methods=['GET'])
def product_details(product_id):
    product = next((product for product in grocery_products if product["id"] == product_id), None)
    if product:
        return jsonify({"product": product})
    else:
        return jsonify({"error": "Product not found"}), 404


# Endpoint 3: Adding new grocery products to the inventory
@app.route('/products', methods=['POST'])
def new_product():
    new_product = {
        "id": len(grocery_products) + 1,
        "name": request.json.get('name'),
        "price": request.json.get('price'),
        "quantity": request.json.get('quantity')
    }
    grocery_products.append(new_product)
    return jsonify({"message": "Product added", "product": new_product}), 201  


if __name__ == '__main__':
    app.run(debug=True)

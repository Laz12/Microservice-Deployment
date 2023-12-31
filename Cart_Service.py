from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# URL of the Product Service
PRODUCT_SERVICE_URL = 'https://product-service-58wv.onrender.com' 

# Sample user cart data (you can use a database in a real application)
user_carts = {
    1: {1: 3},
}

# Endpoint 1: Retrieve current contents of a user’s shopping cart, including product names, quantities, and total prices.
@app.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    user_cart = user_carts.get(user_id, {})
    cart_contents = []

    for product_id, quantity in user_cart.items():
        product_info = get_product_info(product_id)
        if product_info:
            cart_contents.append({
                "product_name": product_info['name'],
                "quantity": quantity,
                "total_price": product_info['price'] * quantity
            })

    return jsonify(cart_contents)

# Endpoint 2: Add a specified quantity of a product to the user’s cart
@app.route('/cart/<int:user_id>/add/<int:product_id>', methods=['POST'])
def add_to_cart(user_id, product_id):
    quantity = request.get_json().get('quantity', 1)

    product_info = get_product_info(product_id)
    if not product_info:
        return jsonify({"error": "The product you're looking for was not found"}), 404

    user_cart = user_carts.setdefault(user_id, {})
    user_cart[product_id] = user_cart.get(product_id, 0) + quantity
    
    return jsonify({"message": f"{quantity} {product_info['name']} were added to cart"}), 201

# Endpoint 3: Remove a specified quantity of a product from the user’s cart
@app.route('/cart/<int:user_id>/remove/<int:product_id>', methods=['POST'])
def remove_from_cart(user_id, product_id):
    quantity = request.get_json().get('quantity', 1)

    product_info = get_product_info(product_id)
    if not product_info:
        return jsonify({"error": "The product you tried to remove was not found"}), 404

    user_cart = user_carts.get(user_id, {})
    if product_id in user_cart:
        user_cart[product_id] = max(user_cart[product_id] - quantity, 0)
        
        if user_cart[product_id] == 0:
            del user_cart[product_id]

    return jsonify({"message": f"{quantity} {product_info['name']} have been removed from cart"}), 200

def get_product_info(product_id):
    response = requests.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}")
    if response.status_code == 200:
        return response.json()
    return None

# Endpoint 4: Update the quantity of a product in the cart
@app.route('/cart/update_product_quantity/<int:product_id>', methods=['PATCH'])
def update_product_quantity_in_cart(product_id):
    data = request.get_json()
    quantity_change = data.get('quantity_change', 0)

    # Update the quantity in the shopping cart
    for _, cart in user_carts.items():
        if product_id in cart:
            current_quantity = cart[product_id]
            new_quantity = current_quantity + quantity_change

            # Check if new_quantity is within acceptable bounds
            if new_quantity >= 0:
                cart[product_id] = new_quantity
            else:
                return jsonify({"error": "Quantity change results in a negative quantity in the cart"}), 400

    # Update the product's quantity in the Product Service
    update_quantity_in_product_service(product_id, quantity_change)
    product_info = get_product_info(product_id)

    if product_info:
        product_name = product_info['name']
    else:
        product_name = "Product"

    return jsonify({"message": f"{quantity_change} units of {product_name} updated in Cart and Product Service"}), 200

def update_quantity_in_product_service(product_id, quantity_change):
    # Send a request to the Product Service to update the product quantity
    data = {"quantity_change": quantity_change}
    response = requests.patch(f"{PRODUCT_SERVICE_URL}/products/update_quantity/{product_id}", json=data)

    if response.status_code != 200:
        return jsonify({"error": "Failed to update product quantity in Product Service"}), 500


if __name__ == '__main__':
    app.run(debug=True, port=8000)




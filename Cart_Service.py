from flask import Flask, jsonify, request

app = Flask(__name__)

cart_contents = [
    {'user_id': 1, 'product_id': 4,'name': 'Apple', 'quantity': 2, 'price_per_item': 10.0},
    {'user_id': 2, 'product_id': 5, 'quantity': 1, 'price_per_item': 20.0}
]


# Endpoint 1: Retrieve current contents of a user’s shopping cart, including product names, quantities, and total prices.
@app.route('/cart/<int:user_id>', methods=['GET'])
def get_content():
    return jsonify({"cart content": cart_contents})


# Endpoint 2: Add a specified quantity of a product to the user’s cart
@app.route('/cart/<int:user_id>/add/<int:product_id>', methods=['POST'])
def new_product(user_id, product_id):
    # Parse the request data to get the quantity
    data = request.get_json()
    quantity = data.get('quantity', 1)  # Default to 1 if not specified
    cart_data = {
        'user_id': user_id,
        'cart': {
            product_id: {
                'product_name': 'Apple',  # Replace with actual product details
                'quantity': quantity
            }
        }
    }
    # cart_contents[item] = cart_contents.get(item, 0) + quantity
    return jsonify({'cart_contents': cart_contents})
 

# Endpoint 3: Remove a specified quantity of a product from the user’s cart
@app.route('/cart/<int:user_id>/remove/<int:product_id>', methods=['POST'])
def remove_product(user_id, product_id):

    # Parse the request data to get the quantity to remove
    data = request.get_json()
    quantity_to_remove = data.get('quantity', 1)  # Default to 1 if not specified

    # Retrieve the user's cart (assuming you have a cart data storage mechanism)
    user_cart = next((content for content in cart_contents if content["user_id"] == user_id), None)

    if user_cart is None:
        return jsonify({'error': f'User {user_id} does not have a cart'}), 404

    # Check if the product is in the user's cart
    if product_id not in user_cart:
        return jsonify({'error': f'Product {product_id} not found in the cart'}), 404

    # Retrieve the current quantity of the product in the cart
    current_quantity = user_cart[product_id]['quantity']

    # Check if the quantity to remove is valid
    if quantity_to_remove <= 0 or quantity_to_remove > current_quantity:
        return jsonify({'error': 'Invalid quantity to remove'}), 400

    # Update the quantity in the cart
    user_cart[product_id]['quantity'] -= quantity_to_remove

    # You may want to remove the product entry from the cart if the quantity reaches 0
    if user_cart[product_id]['quantity'] == 0:
        del user_cart[product_id]

    # Save the updated cart back to the storage mechanism
    save_user_cart(user_id, user_cart)  # Replace with your method to save user's cart

    return jsonify({'message': f'Removed {quantity_to_remove} of product {product_id} from the cart for user {user_id}'})
  


if __name__ == '__main__':
    app.run(debug=True)

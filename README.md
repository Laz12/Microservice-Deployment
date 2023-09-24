# Cart and Product Services URL
- https://cart-service-ikbg.onrender.com
- https://product-service-58wv.onrender.com


# Execute Bash Script for Automated API Testing with Curl Commands
## To test different values for the endpoints, simply edit the relevant variables or parameters in the script to match your test cases.
```bash
./curl.sh
```
## Credentials 
Student: Lazaro Camero Ruiz
Course: CMSC 455 - Software as a Service


# Deploying Flask Services on Render and Testing with cURL

This guide will walk you through deploying two Flask services on Render and testing the endpoints using `curl`. The services include a Cart Service and a Product Service.

## Prerequisites

- [Render](https://render.com/) account

## Deploying the Services on Render

1. **Cart and Product Service Deployment:**

   - Deploy the Cart and Product Services using Render. You can follow Render's documentation for deploying Flask applications.
   - Once deployed, make note of the Cart Service URL, which will be used for testing.
   - https://render.com/docs/deploy-flask ; for a walk through of how to deploy a flask app


## Testing Endpoints with cURL

You can use `cURL` to test the endpoints of both services. Replace the placeholders in the cURL commands with actual values.

### Cart Service Endpoints

- Retrieve current contents of a user’s shopping cart
```bash
curl <Cart_Service_URL>/cart/<user_id>
curl https://cart-service-ikbg.onrender.com/cart/1 
```

- Add a specified quantity of a product to the user’s cart
```bash
curl -X POST -H "Content-Type: application/json" -d '{"quantity": value}' <Cart_Service_URL>/cart/<user_id>/add/<product_id>
curl -X POST -H "Content-Type: application/json" -d '{"quantity": 20}' https://cart-service-ikbg.onrender.com/cart/1/add/1
```

- Remove a specified quantity of a product from the user’s cart
```bash
curl -X POST -H "Content-Type: application/json" -d '{"quantity": 3}' https://your-cart-service-url.com/cart/1/add/5
curl -X POST -H "Content-Type: application/json" -d '{"quantity": 1}' https://cart-service-ikbg.onrender.com/cart/1/remove/1
```

- Update the quantity of a product in the cart
```bash
curl -X PATCH -H "Content-Type: application/json" -d '{"quantity_change": 5}' <Cart_Service_URL>/cart/update_product_quantity/<product_id>
curl -X PATCH -H "Content-Type: application/json" -d '{"quantity_change": 5}' https://cart-service-ikbg.onrender.com/cart/update_product_quantity/1
```

### Product Service Endpoints

- Retrieve list of grocery products, including their names, prices, and quantity in stock
```bash
curl <Product_Service_URL>/products
curl https://product-service-58wv.onrender.com/products
```

- Get details about a specific product by its unique ID
```bash
curl <Product_Service_URL>/products/<product_id>
curl https://product-service-58wv.onrender.com/products/3
```
- Add new grocery products to the inventory
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "New Product", "price": 5.0, "quantity": 10}' <Product_Service_URL>/products
curl -X POST -H "Content-Type: application/json" -d '{"name": "New Product", "price": 5.0, "quantity": 10}' https://product-service-58wv.onrender.com/products
```

- Update quantity of the product
- Use a "negative number" to increment the quantity, and a "positive to decrement" the quantity
```bash
curl -X PATCH -H "Content-Type: application/json" -d '{"quantity_change": 5}' <Product_Service_URL>/products/update_quantity/<product_id>
curl -X PATCH -H "Content-Type: application/json" -d '{"quantity_change": 5}' https://product-service-58wv.onrender.com/products/update_quantity/3
```

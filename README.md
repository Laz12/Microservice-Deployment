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

### Cart and Product Services URL
- https://cart-service-ikbg.onrender.com
- https://product-service-58wv.onrender.com

### Cart Service Endpoints

#### 1. Retrieve the Cart Contents (GET)

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

### Do the same as above for the Product Service as it follows the same concept
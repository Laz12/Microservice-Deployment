# Deploying Flask Services on Render and Testing with cURL

This guide will walk you through deploying two Flask services on Render and testing the endpoints using `curl`. The services include a Cart Service and a Product Service.

## Prerequisites

- [Render](https://render.com/) account
- [cURL](https://curl.se/) installed on your local machine

## Deploying the Services on Render

1. **Cart Service Deployment:**

   - Deploy the Cart Service using Render. You can follow Render's documentation for deploying Flask applications.
   - Once deployed, make note of the Cart Service URL, which will be used for testing.

2. **Product Service Deployment:**

   - Deploy the Product Service using Render, similar to the Cart Service.
   - Note the Product Service URL for testing.

## Testing Endpoints with cURL

You can use `cURL` to test the endpoints of both services. Replace the placeholders in the cURL commands with actual values.

### Cart Service Endpoints

#### 1. Retrieve the Cart Contents (GET)

```bash
curl <Cart_Service_URL>/cart/<user_id>

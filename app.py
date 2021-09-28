from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({"message": "pong!"})

@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "products list"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]}) 
    return jsonify({"message": "Product not found"})

@app.route('/products', methods=['POST'])
def addProduct():
    print(request.json)
    return 'recieved'


if __name__ == '__main__':
    app.run(debug=True, port=3000)
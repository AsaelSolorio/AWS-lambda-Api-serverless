from flask import Flask, jsonify, request
import json
from flask_cors import CORS
import dynamodb_handler as dynamodb


#instantiate CORS
app = Flask("Product Server")
CORS(app)


#error handler
def page_not_found(error):
    return "<h1> Not Found Page </h1>", 404
    
#REST API end-points 
# Example request - http://localhost:5000/get_products - with method GET
@app.route('/get_product/<int:id>', methods=['GET'])
def get_products(id):
    response = dynamodb.get_product(id)
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        
        if ('Item' in response):
            return { 'Item': response['Item'] }

        return { 'msg' : 'Item not found!' }

    return {
        'msg': 'Some error occured',
        'response': response
    }
    
    
# Example request - http://localhost:5000/products - with method POST
@app.route('/add_product', methods=['POST'])
def add_products():
    data = request.get_json()
    # id, title, author = 1001, 'Angels and Demons', 'Dan Brown'

    response = dynamodb.add_product(data['id'], data['name'], data['price'])    
    
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg': 'Added successfully',
        }

    return {  
        'msg': 'Some error occcured',
        'response': response
    }

# Example request - http://localhost:5000/products/144 - with method PUT
@app.route('/update/<int:item_id>', methods=['PUT'])
def update_products(item_id):
    data = request.get_json()

    response = dynamodb.update_product(id, data)

    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg'                : 'Updated successfully',
            'ModifiedAttributes' : response['Attributes'],
            'response'           : response['ResponseMetadata']
        }

    return {
        'msg'      : 'Some error occured',
        'response' : response
    } 

# Example request - http://localhost:5000/products/144 - with method DELETE
@app.route('/delete/<int:item_id>', methods=['DELETE'])
def delete_products(item_id):
    response = dynamodb.delete_product(id)

    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg': 'Deleted successfully',
        }

    return {  
        'msg': 'Some error occcured',
        'response': response
    } 


if __name__=="__main__":
    #Error handlers
    app.register_error_handler(404, page_not_found)
    app.run(host= "0.0.0.0",port=8000,debug=True)

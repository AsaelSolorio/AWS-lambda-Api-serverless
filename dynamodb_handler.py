import boto3
from decouple import config

#import the credentials to our python file
AWS_ACCESS_KEY_ID     = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
REGION_NAME           = config("REGION_NAME")

#Set Client and Resource
client = boto3.client(
    'dynamodb',
    aws_access_key_id     = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name           = REGION_NAME,
)
resource = boto3.resource(
    'dynamodb',
    aws_access_key_id     = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name           = REGION_NAME,
)

#instantiate table in dynamo
Product_Table = resource.Table('products')



#POST method
def add_product(id, name, price):
    response = Product_Table.put_item(
        Item = {
            'id'     : id,
            'name'  : name,
            'price' : price,
        }
    )
    return response
    
#GET method
def get_product(id):
    response = Product_Table.get_item(
        Key = {
            'id'     : id
        },
        AttributesToGet=[
            'name', 
            'price'
        ]
    )
    return response
    
#PUT method
def update_product(id, data:dict):
    response = Product_Table.update_item(
        Key = {
            'id': id
        },
        AttributeUpdates={
            'name': {
                'Value'  : data['name'],
                'Action' : 'PUT' 
            },
            'price': {
                'Value'  : data['price'],
                'Action' : 'PUT'
            }
        },
        ReturnValues = "UPDATED_NEW" 
    )
    return response

#DELETE method
def delete_product(id):
    response = Product_Table.delete_item(
        Key = {
            'id': id
        }
    )
    return response
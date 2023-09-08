         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


we are going to create a simple REST API using flask in AWS Cloud9 for query and creation of
products.
we will use AWS-Dynamodb as database.
We are going to use AWS LAMBDA to create a function with the POST method
and AWS API-GATEWAY for the api methods through INDOMNIA/POSTMAN


![image](https://github.com/AsaelSolorio/AWS-lambda-Api-serverless/assets/112660076/d3938378-f0b5-4baf-8c64-e9e6dccd08ae)



We will create a database using Dynamodb hosted in AWS instance to store information about products. we will create .env file to configure the connection.
``` batch
AWS_ACCESS_KEY_ID='<YOUR DATA HERE>'
AWS_SECRET_ACCESS_KEY='<YOUR DATA HERE>'
REGION_NAME='<YOUR DATA HERE>'
```

We will be using the HTTP methods through Insomnia requests

- GET
- POST
- PUT
- DELETE

We will be using the HTTP POST method through AWS-Lambda.
set up  services for the application
-Dynamo DB
-IAM policies fro the user
-Lambda Function:
-API Gateway:



next, create a virtual venv
``` batch
python -m venv venv
source venv/bin/activate
```
next, you can scaffold the Makefile to install all the libraries
``` batch
make install
```



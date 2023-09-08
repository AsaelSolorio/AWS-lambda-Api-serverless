install:
		pip install --upgrade pip 
		pip install -r requirements.txt
		pip install psycopg-binary
		pip install SQLAlchemy
		pip install flask-cors
		pip install python-decouple
		pip install python-dotenv
		pip install boto3

	
	

lint:
		pylint --disable=R,C app.py
	
format:
		black *.py
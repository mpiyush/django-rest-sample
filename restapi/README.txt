1) Setup
	Required Packages:
		django 1.4 or higher
		django-restframework
		requests

2) Running the tool
	i) Execute 'python manage.py runserver $HOST:$PORT'
		where host and port are 127.0.0.1:8000 by default
	
	ii) Browser to $HOST:$PORT to view REST API
	
	iii) a) http://127.0.0.1:8000/server/?my_lat=100&my_long=80
			here my_lat and my_long can be substitued by your latitude and longitude to obtain a list of servers in order of distance
		 b) http://127.0.0.1:8000/server/ 
			a form is avaiable to add data using POST
		 c) http://127.0.0.1:8000/server/1
			a DELETE request can be sent to any of the rows of the data
	
3) Running tests
	REST Tests
	i) Execute 'python manage.py testserver mydata.json' in one window to start a testserver with test data
	ii) Execute 'python restapi\test_RESTAPI.py' in another windown to run tests
	DB Tests for django models
	i) Execute 'python manage.py test restapi'
	

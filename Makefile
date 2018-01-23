setup:
	echo "setup application"
	pip install -r requirements.txt -r requirements_dev.txt

run:
	echo "application running"
	FLASK_APP=algorithm-services.py flask run

lint:
	flake8

test:
	echo "test application"
	nosetests -v

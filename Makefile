setup:
	echo "setup application"
	pip install -r requirements.txt -r requirements_dev.txt

run:
	echo "application running"
	python algorithm-services.py
	
lint:
	flake8

test:
	echo "test application"
	nosetests -v

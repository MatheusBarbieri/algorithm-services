setup:
	echo "setup application"
	pip install -r requirements.txt -r requirements_dev.txt

run:
	echo "application running"

test:
	echo "test application"
	nosetests -v

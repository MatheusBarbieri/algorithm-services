setup:
	pip install -r requirements.txt -r requirements_dev.txt

run:
	python server.py

lint:
	flake8

test:
	nosetests -v

setup:
	pip install -r requirements.txt -r requirements_dev.txt

run:
	python server.py

lint:
	flake8

test:
	nosetests -v

docker-run: docker-clean docker-build
	docker run -p 5000:5000 --name algorithm_services algorithm_services

docker-build:
	docker build -t algorithm_services .

docker-clean:
	-docker stop algorithm_services
	-docker rm algorithm_services

bench:
	wrk -t1 -c1 -d60s http://127.0.0.1:8080/fizzbuzz/15 -s benchmark/wrk_results/results.lua --latency
	wrk -t1 -c25 -d60s http://127.0.0.1:8080/fizzbuzz/15 -s benchmark/wrk_results/results.lua --latency
	wrk -t1 -c50 -d60s http://127.0.0.1:8080/fizzbuzz/15 -s benchmark/wrk_results/results.lua --latency
	wrk -t12 -c400 -d60s http://127.0.0.1:8080/fizzbuzz/15 -s benchmark/wrk_results/results.lua --latency

	wrk -t1 -c1 -d60s http://127.0.0.1:8080/clock_angle/15/45 -s benchmark/wrk_results/results.lua --latency
	wrk -t1 -c25 -d60s http://127.0.0.1:8080/clock_angle/15/45 -s benchmark/wrk_results/results.lua --latency
	wrk -t1 -c50 -d60s http://127.0.0.1:8080/clock_angle/15/45 -s benchmark/wrk_results/results.lua --latency
	wrk -t12 -c400 -d60s http://127.0.0.1:8080/clock_angle/15/45 -s benchmark/wrk_results/results.lua --latency

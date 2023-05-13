.PHONY: start stop test
.SILENT: start stop test

start:
	docker-compose up --build -d

stop:
	docker-compose down

test:
	env/bin/python -m unittest discover

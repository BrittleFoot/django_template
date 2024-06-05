deps:
	pip-compile requirements.in
	pip-compile requirements-dev.in
	pip-sync requirements.txt requirements-dev.txt

lint:
	ruff check src

fix:
	ruff format src && ruff check src --fix

test:
	pytest src $(ARGS)

start:
	docker-compose up -d
	cd src && ./manage.py runserver

# image:
# 	docker build -t test .

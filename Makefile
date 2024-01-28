deps:
	pip-compile requirements.in
	pip-compile dev-requirements.in
	pip-sync requirements.txt dev-requirements.txt

lint:
	ruff src $(ARGS)

fix:
	ruff src --fix

test:
	pytest src $(ARGS)

start:
	docker-compose up -d
	cd src && ./manage.py runserver

# image:
# 	docker build -t test .

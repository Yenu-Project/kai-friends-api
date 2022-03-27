SHELL := /bin/bash
include ./.env

rundb:
	docker compose -f docker-compose.dev.yml up -d

downdb:
	docker compose -f docker-compose.dev.yml down

init:
	mysql -u ${KAIFRIENDS_DB_USER} -P ${KAIFRIENDS_DB_PORT} -h ${KAIFRIENDS_DB_HOST} --password=${KAIFRIENDS_DB_PASSWORD} -e 'CREATE DATABASE kai_friends CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;'
	python manage.py migrate

migrate:
	python manage.py makemigrations
	python manage.py migrate

superuser:
	python manage.py createsuperuser

run:
	python manage.py runserver 0.0.0.0:9000

shell:
	python manage.py shell -i bpython

env: # use for local & might not be ~/.bachrc (ex. .zshrc etc.)
	git clone git://github.com/inishchith/autoenv.git ~/.autoenv
	echo 'source ~/.autoenv/activate.sh' >> ~/.bashrc
	source ~/.bashrc

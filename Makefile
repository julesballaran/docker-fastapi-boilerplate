run:
	uvicorn main:app --reload

insall_packages:
	pip install -r requirements.txt

build:
	docker build -t jules44/docker-fastapi-boilerplate:latest .

push:
	docker push jules44/docker-fastapi-boilerplate:latest

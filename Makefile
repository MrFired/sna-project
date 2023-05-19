init:
	pip3 install pipenv
	pipenv install -d
	pip3 install pre-commit
	pipenv run pre-commit install
	pipenv run pre-commit install-hooks

build:
	docker build . -t hoyo

run: 
	docker run -p 5000:5000 --rm hoyo

lint:
	pipenv run flake8 src
	pipenv run refurb src

typecheck:
	pipenv run pyright
	
deploy:
	minikube start
	minikube image build -t hoyo .
	minikube kubectl -- create -f deployment.yaml
	minikube kubectl -- wait --for=condition=available deployment/hoyoweb
	minikube kubectl -- port-forward deployment/hoyoweb 5000:5000 &

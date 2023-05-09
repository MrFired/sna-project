init:
	pip3 install pipenv
	pipenv install -d
	pip3 install pre-commit
	pipenv run pre-commit install
	pipenv run pre-commit install-hooks
	
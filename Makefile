install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C hello.py ##disable recommended & config warnings, keeps warnings and errors

format:
	black

test:
	python -m pytest -vv --cov=hello test_hello.py
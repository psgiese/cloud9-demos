install:
	pip install --upgrade pip &&\
		pip install -r /home/ec2-user/environment/cloud9-demos/requirements.txt

lint:
	pylint --disable=R,C *.py ##disable recommended & config warnings, keeps warnings and errors

format:
	black *.py

test:
	python -m pytest -vv --cov=. #daily_coding_problems/tests/

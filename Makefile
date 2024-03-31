install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	isort .
	black .

all: install format

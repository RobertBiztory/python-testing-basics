run:
	python src/thething/main.py


test:
	pytest -v

install:
	pip install -e .
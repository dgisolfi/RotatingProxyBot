# RotatingProxyBot
# Author: Daniel Nicolas Gisolfi

repo=RotatingProxyBot
version=0.0.1

intro:
	@echo "\nRotatingProxyBot v$(version)"

init:
	@python3 -m pip install -r requirements.txt

clean:
	-rm -r ./build
	-rm -r ./dist
	-rm -r ./$(repo).egg-info

test:
	@python3 -m pytest -s

build:
	@python setup.py sdist

publish:
	@python3 -m twine upload dist/*

install:
	@python3 -m pip install .

uninstall:
	@python3 -m pip uninstall $(repo)

.PHONY: init clean test build
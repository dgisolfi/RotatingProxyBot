# RotatingProxyBot
# Author: Daniel Nicolas Gisolfi

repo=RotatingProxyBot
version=0.0.1

intro:
	@echo "\nRotatingProxyBot v$(version)"

# init:
#     @python3 -m pip install -r requirements.txt

clean:
	-rmdir -r ./build
	-rmdir -r ./dist
	-rm ./$(repo).egg-info

test:
	@python3 -m pytest

build:
	@python setup.py sdist

publish:
	@python3 -m twine upload dist/*

install:
	@python setup.py install

.PHONY: clean test build
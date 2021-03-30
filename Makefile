black: ## black format every python file to line length 100
	find . -type f -name "*.py" | xargs black --line-length=100;
	find . -type d -name "__pycache__" | xargs rm -r;

flake: ## flake8 every python file except ./craigslist_meta/metadata.py
	find . -type f -name "*.py" -a ! -name "metadata.py" | xargs flake8;

pylint: ## pylint every python file except ./craigslist_meta/metadata.py
	find . -type f -name "*.py" -a ! -name "metadata.py" | xargs pylint; 

setup: ## build package distribution files
	python ./setup.py sdist;

clean: ## remove package distribution files and pycache
	rm -rf ./python_craigslist_meta.egg-info ./dist ./build;
	find . -type d -name "__pycache__" | xargs rm -r;

upload: ## upload package distribution files to pypi
	twine upload ./dist/*;
	make clean;

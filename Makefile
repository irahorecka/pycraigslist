black: ## black format every python file to line length 100
	find . -type f -name "*.py" | xargs black --line-length=100;
	find . -type d -name "__pycache__" | xargs rm -r;

flake: ## flake8 every python file
	find . -type f -name "*.py" -a | xargs flake8;

pylint: ## pylint every python file
	find . -type f -name "*.py" -a | xargs pylint; 

setup: ## build package distribution files
	flit build;

clean: ## remove package distribution files and pycache
	rm -rf ./pycraigslist.egg-info ./dist ./build;
	find . -type d -name "__pycache__" | xargs rm -r;

upload: ## upload package distribution files to pypi
	flit publish;

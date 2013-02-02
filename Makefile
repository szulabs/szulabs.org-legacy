ASSETS_COMPONENTS_DIR = szulabs/assets/components/

build:
	python setup.py build

release:
	git checkout release
	git pull origin release
	rm -rf $(ASSETS_COMPONENTS_DIR)
	bower install
	git add $(ASSETS_COMPONENTS_DIR)
	@echo ""
	@echo "Now you can commit and push to your repository."
	@echo "Don't forget to bump the version."

clean:
	find . -type f -name "*.pyc" -exec rm -f {} +
	rm -rf ./*.{egg, egg-info} ./build ./dist

venv:
	rm -rf ./venv
	virtualenv -p python2.7 --distribute venv
	echo "szulabs-dev" > ./venv/__name__
	. ./venv/bin/activate; pip install -r requirements.txt

.PHONY: build release clean venv

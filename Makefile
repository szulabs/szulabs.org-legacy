ASSETS_COMPONENTS_DIR = szulabs/assets/components/

release:
	git checkout release
	git pull origin release
	rm -rf $(ASSETS_COMPONENTS_DIR)
	bower install
	git add $(ASSETS_COMPONENTS_DIR)
	@echo ""
	@echo "Now you can commit and push to your repository."
	@echo "Don't forget to bump the version."

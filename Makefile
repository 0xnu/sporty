.PHONY: help pull dev deactivate acp tag release status log

# Help message
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\\033[36m%-30s\\033[0m %s\\n", $$1, $$2}'

VERSION=0.0.0
BRANCH=main
COMMIT_MSG ?= "Makefile"
RELEASE_NOTE ?= "Release Note"

# Pull latest changes
pull: ## Pull latest changes
	git pull origin $(BRANCH)


dev: ## Create virtual environment and install dependencies
	@python3 -m venv .venv
	@pip3 install -r requirements.txt && python3 -m pip install --upgrade pip

activate: ## Print instructions to activate the virtual environment
	@echo "To activate the virtual environment, use 'source .venv/bin/activate' command in your shell"

deactivate: ## Deactivate virtual environment
	@echo "To deactivate virtual environment, use 'deactivate' command in your shell"

acp: ## Add, Commit and Push
	@git add .
	@git commit -s -m $(COMMIT_MSG)
	@git push

tag: ## Tag
	@git tag "v$(VERSION)"
	@git push --tag

release: ## Release
	@if command -v gh &> /dev/null; then \
		gh release create "v$(VERSION)" --title "v$(VERSION)" --notes $(RELEASE_NOTE); \
	else \
		echo "gh command not found. Please install GitHub CLI to create a release."; \
	fi

# Check the status
status: ## Check the status
	git status

# Show the commit logs
log: ## Show the commit logs
	git log

.DEFAULT_GOAL := help
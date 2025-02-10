.PHONY: * # Using Make as a simple task runner

deps: ## Install dependencies
	. .venv/bin/activate; pip install --upgrade pip;
	. .venv/bin/activate; pip --require-virtualenv install -r requirements.txt -r requirements-dev.txt; 
	. .venv/bin/activate; pip check;

start: ## Start service
	. .venv/bin/activate; python src/api.py 

docker-build: ## Build image of service 
	docker build -t receipt-processor .

docker-start: ## Run containerized service
	docker run -p 8000:8000 receipt-processor 

fmt: ## Format code 
	. .venv/bin/activate; ruff check --fix .
	. .venv/bin/activate; ruff format .

lint: ## Run linters 
	. .venv/bin/activate; mypy .

test: ## Run unit and integration tests 
	. .venv/bin/activate; pytest tests 

help: ## Show this help
	@grep -E '^([a-zA-Z_-]|\\:)+:.*?## .*$$' $(MAKEFILE_LIST) | sort | tr -d '\' | awk 'BEGIN {FS = ": .*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

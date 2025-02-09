# Receipt Processor 

Hello, Fetch! 

## Usage

For ease of use, all functionality has been encapsulated in a Makefile.

You'll need either Docker OR Python >=3.9 to run the service. 

### Getting Started

## Docker

```bash
make docker-build
make docker-start
```

## Local Development

**IMPORTANT!!!** All utilities and commands require the creation of a virtual environment:
```bash
# Virtual environment MUST be named ".venv"
python -m venv .venv  
source .venv/bin/activate

make help  # List of available commands

make deps  # Install prod and dev dependencies

make fmt   # Format code (ruff)
make lint  # Lint code (mypy)
make test  # Run test suite
```

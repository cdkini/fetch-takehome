# Receipt Processor 

Hello, Fetch! Contained herein is my receipt processor API.

If you're pressed for time and just want to check the API's functionality, look at the instructions below.

If you have more time and want to dive into the architecture, please see [my thoughts](./ARCHITECTURE.md).

## Usage

For ease of use, all functionality has been encapsulated in a Makefile.

You'll need either Docker OR Python >=3.9 to run the service. 

## Getting Started

### Docker

If you're using Docker, you can simply build the image and spin up a container with the service:
```bash
make docker-build
make docker-start
```

### Local Development

If you're working with the API locally, you might find these commands helpful:
```bash
# **IMPORTANT!!!** All utilities and commands require the creation of a virtual environment:
python -m venv .venv  
source .venv/bin/activate

make help  # List of available commands

make deps  # Install prod and dev dependencies

make fmt   # Format code (ruff)
make lint  # Lint code (mypy)
make test  # Run test suite
```

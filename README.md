# Receipt Processor 

Hello, Fetch! 

In case you're reviewing this and you're pressed for time, please take a look at:
1. This README
2. The `src/` directory

---

## Spec (in my own words)

Given three JSON/EDI file pairings and a basic script to kick things off, build a library that converts from one claims submission format to another, in order to submit to multiple clearinghouses. The spec is extensive but largely use the three examples as the source of truth for scope and correctness.

---

## Usage

For ease of use, all functionality has been encapsulated in a Makefile.

You'll need the following dependencies:
1. Python >=3.9 for the actual library
3. OPTIONAL: Node & NPM if choosing to open the docs site

### Getting Started

**IMPORTANT!!!** All utilities and commands require the creation of a virtual environment:
```bash
# Virtual environment MUST be named ".venv"
python -m venv .venv  
source .venv/bin/activate

# List of available commands
make help
```

### Installation 

If it is your first time running the library, you'll need to run `make deps`:
```bash
make deps   # Install prod and dev dependencies
```

### Docs

Docs are powered by [docsify](https://docsify.js.org/#/) and require an additional NPM dep:
```bash
npm i docsify-cli  # Install docsify
make docs          # Open docs site (localhost:3000/)

# Alternatively, you can run the following without needing NPM but that's less fun >:( 
(cd docs && python -m http.server 3000)
```

### Development

Developer utilities (formatting, linting, and testing) are as follows: 
```bash
make fmt   # Format code (ruff)
make lint  # Lint code (mypy)
make test  # Run test suite
```

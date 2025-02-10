# Receipt Processor 

Hello, Fetch! Contained herein is my receipt processor API.

If you're pressed for time and just want to check the API's functionality, look at the Docker instructions below.

If you have more time and want to dive into the architecture and some additional thoughts, please look at the end of this file. 

## Table of Contents

- [Usage](#usage)
   * [Docker](#docker)
   * [Local Development](#local-development)
- [Architecture](#architecture)
- [Next Steps ](#next-steps)

## Usage

For ease of use, all functionality has been encapsulated in a Makefile.

You'll need either Docker OR Python >=3.9 to run the service. 

### Docker

If you're using Docker, you can simply build the image and spin up a container with the service:
```bash
# Will spin up on http://0.0.0.0:8000/
# OpenAPI docs can be found at /docs
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

## Architecture

I've designed this API to adhere to Clean Architecture practices as best as possible. This should keep the code reasonably decoupled, maintainable, and open for easy extension.

The primary components are as follows:
- Providers
    - Responsible for storing and retrieving domain objects (data access layer) - we use a SQLite DB here but any relational database will work.
- Apps
    - Encapsulates core business logic and uses one or more providers to deal with object CRUD (business logic layer).
- Handlers
    - Responsible for routing and acting as the entry and exit point for all requests. This takes the form of a REST router in this API.
- Services
    - Instantiates all other components (providers, apps, and handlers) and uses dependency injection to set up the API. 

Each discrete section of our domain will have its own set of these components (just receipts for now).

## Next Steps 

I've timeboxed this effort but there are a number of things I would do to follow up on this API:
- Add authn/authz (JWT or OAuth)
- Implement some kind of rate limiting (see test script in `scripts/`)
- More test coverage and better segregation of unit/integration/e2e
- More thorough configuration and support for `.env`

# Architecture

I've designed this API to adhere to Clean Architecture practices as best as possible. This should keep the code reasonably decoupled, maintainable, and open for easy extension.

The primary components are as follows:
- Providers
    - Responsible for storing and retrieving domain objects (data access layer).
- Apps
    - Encapsulates core business logic and uses one or more Providers to deal with object CRUD (business logic layer).
- Handlers
    - Responsible for routing and acting as the entry and exit point for all requests. This takes the form of a REST router in this API.
- Services
    - Instantiates all other components (providers, apps, and handlers) and uses dependency injection to set up the API. 

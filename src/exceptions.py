class BaseError(Exception):
    pass  # Base class for all exceptions in this module


class ProviderError(BaseError):
    pass


class AppError(BaseError):
    pass

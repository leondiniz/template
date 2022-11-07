
class ValidationException(Exception):
    """ValidationException"""

    def __init__(self, message):
        self.message = message


class BussinesException(Exception):
    def __init__(self, message):
        self.message = message


class UnauthorizedException(BussinesException):
    def __init__(
        self,
        message="You do not have permission to perform this action."
    ):
        self.message = message

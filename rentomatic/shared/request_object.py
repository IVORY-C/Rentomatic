from typing import List, Dict

class RequestObject():
    def __nonzero__(self):
        raise NotImplementedError

class InvalidRequestObject(RequestObject):

    def __init__(self) -> None:
        self.errors = [] # type: List[Dict[str, str]]

    def add_error(self, parameter : str, message : str) -> None:
        self.errors.append({'parameter': parameter, 'message': message})

    def has_errors(self) -> bool:
        return len(self.errors) > 0

    def __nonzero__(self) -> bool:
        return False

    __bool__ = __nonzero__


class ValidRequestObject(RequestObject):

    @classmethod
    def from_dict(cls, adict: Dict[str, str]):
        raise NotImplementedError

    def __nonzero__(self) -> bool:
        return True

    __bool__ = __nonzero__

from rentomatic.shared import response_object as res


class UseCase(object):

    def execute(self, request_object: str) -> "res.ResponseFailure": 
        if not request_object:
            return res.ResponseFailure.build_from_invalid_request_object(request_object)
        try:
            return self.process_request(request_object)
        except Exception as exc:
            return res.ResponseFailure.build_system_error(
                "{}: {}".format(exc.__class__.__name__, "{}".format(exc)))

    def process_request(self, request_object: str):
        raise NotImplementedError(
            "process_request() not implemented by UseCase class")

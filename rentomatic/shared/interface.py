
class StorageRepos(object):
    def list(self, filters):
        raise NotImplementedError

class Filters(object):
    def items(self):
        raise NotImplementedError

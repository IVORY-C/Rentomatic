import collections

from rentomatic.shared import request_object as req
from typing import Dict, Union, Optional

class StorageRoomListRequestObject(req.ValidRequestObject):

    def __init__(self, filters: Optional[str] = None):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict : Dict[str, str]) -> Union["req.InvalidRequestObject", "StorageRoomListRequestObject"]: 
        invalid_req = req.InvalidRequestObject()

        if 'filters' in adict and not isinstance(adict['filters'], collections.Mapping):
            invalid_req.add_error('filters', 'Is not iterable')

        if invalid_req.has_errors():
            return invalid_req

        return StorageRoomListRequestObject(filters=adict.get('filters', ""))

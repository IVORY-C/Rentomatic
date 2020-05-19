import json
from rentomatic.domain import storageroom as sr
from typing import Dict, Union, Any


class StorageRoomEncoder(json.JSONEncoder):

    def default(self, o: sr.StorageRoom) -> Dict[str, Any]:
        try:
            to_serialize = {
                'code': str(o.code),
                'size': o.size,
                'price': o.price,
                "latitude": o.latitude,
                "longitude": o.longitude,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)

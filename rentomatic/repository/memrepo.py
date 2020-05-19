from rentomatic.domain import storageroom as sr
from rentomatic.shared import interface as itf
from typing import Dict, List, Union, Optional, Any, Iterable



class MemRepo:

    def __init__(self, entries: List[str] = None):
        self._entries = []
        if entries:
            self._entries.extend(entries)

    def _check(self, element, key: str, value: Any) -> bool:
        if '__' not in key:
            key = key + '__eq'

        key, operator = key.split('__')

        if operator not in ['eq', 'lt', 'gt']:
            raise ValueError('Operator {} is not supported'.format(operator))

        operator = '__{}__'.format(operator)

        if key in ['size', 'price']:
            return getattr(element[key], operator)(int(value))
        elif key in ['latitude', 'longitude']:
            return getattr(element[key], operator)(float(value))

        return getattr(element[key], operator)(value)

    def list(self, filters: Optional[dict] = None) -> List[sr.StorageRoom]:
        if not filters:
            result = self._entries
        else:
            result = [] 
            result.extend(self._entries)

            for key, value in filters.items():
                result = [e for e in result if self._check(e, key, value)]

        return [sr.StorageRoom.from_dict(r) for r in result] 

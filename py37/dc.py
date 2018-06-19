from dataclasses import dataclass, field
import typing
import uuid

@dataclass
class Customer(object):
    id: int
    name: str
    address: str

@dataclass(frozen=True, order=True)
class CustomerOrder(object):
    id: uuid.UUID = field(compare=false, default_factory, init=false)
    value: float = field(compare = True)
    product: str = field(compare = False)

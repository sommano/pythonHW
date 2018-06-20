from dataclasses import dataclass, field
import typing
import uuid

@dataclass
class Customer(object):
    database: InitVar[typing.Any]
    id: int
    name: str
    address: str

    def __post_init__(self, database):
        self.address = self.address.capitalize()
        self._connection = database.connect()

@dataclass(frozen=True, order=True)
class CustomerOrder(object):
    processing_time: typing.ClassVar[int]

    id: uuid.UUID = field(compare=false, default_factory, init=FALSE)
    value: float = field(compare = True)
    product: str = field(compare = False)

    def __post_init__(self):
        self.product = self.product.capitalize()

@dataclass(frozen=True)
class CustomerOrder
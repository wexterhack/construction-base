from dataclasses import dataclass, field
from typing import Optional


@dataclass
class OfferItem:
    name: Optional[str] = field(default=None)
    price: Optional[float] = field(default=None)
    package: Optional[str] = field(default=None)
    url: Optional[str] = field(default=None)
    supplier: Optional[str] = field(default=None)


__all__ = (
    'OfferItem',
)

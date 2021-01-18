from typing import Union

from garage.permit import Permit
from garage.vehicle import Vehicle


class ParkingSpace:
    compact: bool
    required_permit: Union[Permit, int]
    vehicle: Vehicle

    def __init__(
        self,
        compact: bool = None,
        required_permit: Union[Permit, int] = None,
        vehicle: Vehicle = None,
    ):
        self.compact = compact or False
        self.required_permit = required_permit or Permit.NONE
        self.vehicle = vehicle or None

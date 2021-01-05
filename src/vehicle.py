from uuid import uuid4
from typing import Union

from src.permit import Permit
from src.vehicle_type import VehicleType


class Vehicle:
    vehicle_type: VehicleType
    vehicle_id: str
    permit: Permit

    def __init__(
        self,
        vehicle_type: VehicleType = None,
        vehicle_id: str = None,
        permit: Union[Permit, int] = None,
    ):
        self.vehicle_type = vehicle_type or VehicleType.Car
        self.vehicle_id = vehicle_id or str(uuid4())
        self.permit = permit or Permit.NONE

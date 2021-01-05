from typing import List

from src.parking_level import ParkingLevel
from src.vehicle import Vehicle


class Garage:
    levels: List[ParkingLevel]

    def __init__(self, levels: List[ParkingLevel] = None):
        self.levels = levels or []

    def add_vehicles(self, vehicles: List[Vehicle] = None) -> List[Vehicle]:
        return []

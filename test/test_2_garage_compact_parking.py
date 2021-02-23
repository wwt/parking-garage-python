from typing import List

from garage.garage import Garage
from garage.parking_level import ParkingLevel
from garage.parking_space import ParkingSpace
from garage.vehicle import Vehicle
from garage.vehicle_type import VehicleType
from test.utils import TestHelpers


def test_standard_cars_are_rejected_from_compact_parking_space():
    parking_level_1 = ParkingLevel(
        spaces=[ParkingSpace(compact=True), ParkingSpace(compact=True)]
    )
    parking_level_2 = ParkingLevel(
        spaces=[ParkingSpace(compact=True), ParkingSpace(compact=True)]
    )
    parking_level_3 = ParkingLevel(
        spaces=[ParkingSpace(compact=True), ParkingSpace(compact=True)]
    )

    garage = Garage(levels=[parking_level_1, parking_level_2, parking_level_3])

    vehicle_1 = Vehicle(vehicle_type=VehicleType.Compact)
    vehicle_2 = Vehicle(vehicle_type=VehicleType.Car)
    vehicle_3 = Vehicle(vehicle_type=VehicleType.Car)
    vehicle_4 = Vehicle(vehicle_type=VehicleType.Compact)
    vehicle_5 = Vehicle(vehicle_type=VehicleType.Car)
    vehicle_6 = Vehicle(vehicle_type=VehicleType.Car)

    expected_rejected_vehicles: List[Vehicle] = [
        vehicle_2,
        vehicle_3,
        vehicle_5,
        vehicle_6,
    ]

    actual_rejected_vehicles = garage.add_vehicles(
        [vehicle_1, vehicle_2, vehicle_3, vehicle_4, vehicle_5, vehicle_6]
    )

    TestHelpers.assert_expected_vehicles_are_rejected(
        actual=actual_rejected_vehicles, expected=expected_rejected_vehicles
    )


def test_trucks_are_rejected_from_compact_parking_space():
    parking_level_1 = ParkingLevel(
        spaces=[ParkingSpace(compact=True), ParkingSpace(compact=True)]
    )
    parking_level_2 = ParkingLevel(
        spaces=[ParkingSpace(compact=True), ParkingSpace(compact=True)]
    )
    parking_level_3 = ParkingLevel(
        spaces=[ParkingSpace(compact=True), ParkingSpace(compact=True)]
    )

    garage = Garage(levels=[parking_level_1, parking_level_2, parking_level_3])

    vehicle_1 = Vehicle(vehicle_type=VehicleType.Compact)
    vehicle_2 = Vehicle(vehicle_type=VehicleType.Truck)
    vehicle_3 = Vehicle(vehicle_type=VehicleType.Truck)
    vehicle_4 = Vehicle(vehicle_type=VehicleType.Truck)
    vehicle_5 = Vehicle(vehicle_type=VehicleType.Compact)
    vehicle_6 = Vehicle(vehicle_type=VehicleType.Truck)

    expected_rejected_vehicles: List[Vehicle] = [
        vehicle_2,
        vehicle_3,
        vehicle_4,
        vehicle_6,
    ]

    actual_rejected_vehicles = garage.add_vehicles(
        [vehicle_1, vehicle_2, vehicle_3, vehicle_4, vehicle_5, vehicle_6]
    )

    TestHelpers.assert_expected_vehicles_are_rejected(
        actual=actual_rejected_vehicles, expected=expected_rejected_vehicles
    )


def test_compact_vehicles_are_first_prioritized_into_compact_parking_space():
    parking_level_1 = ParkingLevel(
        spaces=[ParkingSpace(compact=True), ParkingSpace(compact=False)]
    )
    parking_level_2 = ParkingLevel(
        spaces=[ParkingSpace(compact=False), ParkingSpace(compact=True)]
    )
    parking_level_3 = ParkingLevel(
        spaces=[ParkingSpace(compact=False), ParkingSpace(compact=False)]
    )

    garage = Garage(levels=[parking_level_1, parking_level_2, parking_level_3])

    vehicle_1 = Vehicle(vehicle_type=VehicleType.Car)
    vehicle_2 = Vehicle(vehicle_type=VehicleType.Compact)
    vehicle_3 = Vehicle(vehicle_type=VehicleType.Compact)
    vehicle_4 = Vehicle(vehicle_type=VehicleType.Truck)
    vehicle_5 = Vehicle(vehicle_type=VehicleType.Compact)
    vehicle_6 = Vehicle(vehicle_type=VehicleType.Car)

    expected_vehicles_on_level_1: List[Vehicle] = [vehicle_2, vehicle_1]
    expected_vehicles_on_level_2: List[Vehicle] = [vehicle_4, vehicle_3]
    expected_vehicles_on_level_3: List[Vehicle] = [vehicle_5, vehicle_6]

    garage.add_vehicles(
        [vehicle_1, vehicle_2, vehicle_3, vehicle_4, vehicle_5, vehicle_6]
    )

    TestHelpers.assert_expected_parking_placement(
        levels=garage.levels,
        expected_levels=[
            expected_vehicles_on_level_1,
            expected_vehicles_on_level_2,
            expected_vehicles_on_level_3,
        ],
    )

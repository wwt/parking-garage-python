from typing import List

from garage.garage import Garage
from garage.parking_level import ParkingLevel
from garage.parking_space import ParkingSpace
from garage.vehicle import Vehicle
from garage.permit import Permit
from garage.vehicle_type import VehicleType
from test.utils import TestHelpers


def test_vehicles_without_disability_permits_are_rejected_from_disability_parking_spaces():
    parking_space_a = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_b = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_c = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_d = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_e = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_f = ParkingSpace(required_permit=Permit.DISABILITY)

    parking_level_1 = ParkingLevel(spaces=[parking_space_a, parking_space_b])
    parking_level_2 = ParkingLevel(spaces=[parking_space_c, parking_space_d])
    parking_level_3 = ParkingLevel(spaces=[parking_space_e, parking_space_f])

    garage = Garage(levels=[parking_level_1, parking_level_2, parking_level_3])

    vehicle_1 = Vehicle(permit=Permit.DISABILITY)
    vehicle_2 = Vehicle(permit=Permit.PREMIUM)
    vehicle_3 = Vehicle(permit=Permit.PREMIUM)
    vehicle_4 = Vehicle(permit=Permit.NONE)
    vehicle_5 = Vehicle(permit=Permit.DISABILITY)
    vehicle_6 = Vehicle(permit=Permit.PREMIUM)

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


def test_vehicles_with_disability_permits_are_added_to_disability_parking_spaces():
    parking_space_a = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_b = ParkingSpace()
    parking_space_c = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_d = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_e = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_f = ParkingSpace()

    parking_level_1 = ParkingLevel(spaces=[parking_space_a, parking_space_b])
    parking_level_2 = ParkingLevel(spaces=[parking_space_c, parking_space_d])
    parking_level_3 = ParkingLevel(spaces=[parking_space_e, parking_space_f])

    garage = Garage(levels=[parking_level_1, parking_level_2, parking_level_3])

    vehicle_1 = Vehicle()
    vehicle_2 = Vehicle(permit=Permit.DISABILITY | Permit.PREMIUM)
    vehicle_3 = Vehicle(permit=Permit.DISABILITY)
    vehicle_4 = Vehicle()
    vehicle_5 = Vehicle()
    vehicle_6 = Vehicle(permit=Permit.DISABILITY)

    expected_vehicles_on_level_1: List[Vehicle] = [vehicle_2, vehicle_1]
    expected_vehicles_on_level_2: List[Vehicle] = [vehicle_3, vehicle_6]
    expected_vehicles_on_level_3: List[Vehicle] = [None, vehicle_4]

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


def test_vehicles_with_disability_permits_do_not_take_priority_over_non_permitted_spaces():
    parking_space_a = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_b = ParkingSpace()
    parking_space_c = ParkingSpace()
    parking_space_d = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_e = ParkingSpace()
    parking_space_f = ParkingSpace()

    parking_level_1 = ParkingLevel(spaces=[parking_space_a, parking_space_b])
    parking_level_2 = ParkingLevel(spaces=[parking_space_c, parking_space_d])
    parking_level_3 = ParkingLevel(spaces=[parking_space_e, parking_space_f])

    garage = Garage(levels=[parking_level_1, parking_level_2, parking_level_3])

    vehicle_1 = Vehicle()
    vehicle_2 = Vehicle(permit=Permit.DISABILITY)
    vehicle_3 = Vehicle(permit=Permit.DISABILITY)
    vehicle_4 = Vehicle()
    vehicle_5 = Vehicle()
    vehicle_6 = Vehicle(permit=Permit.DISABILITY)
    vehicle_7 = Vehicle(permit=Permit.DISABILITY)

    expected_vehicles_on_level_1: List[Vehicle] = [vehicle_2, vehicle_1]
    expected_vehicles_on_level_2: List[Vehicle] = [vehicle_4, vehicle_3]
    expected_vehicles_on_level_3: List[Vehicle] = [vehicle_5, vehicle_6]

    garage.add_vehicles(
        [vehicle_1, vehicle_2, vehicle_3, vehicle_4, vehicle_5, vehicle_6, vehicle_7]
    )

    TestHelpers.assert_expected_parking_placement(
        levels=garage.levels,
        expected_levels=[
            expected_vehicles_on_level_1,
            expected_vehicles_on_level_2,
            expected_vehicles_on_level_3,
        ],
    )


def test_compact_vehicles_with_disability_permits_are_first_prioritized_into_disability_parking_spaces():
    parking_space_a = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_b = ParkingSpace(compact=True)
    parking_space_c = ParkingSpace(compact=True)
    parking_space_d = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_e = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_f = ParkingSpace(compact=True)

    parking_level_1 = ParkingLevel(spaces=[parking_space_a, parking_space_b])
    parking_level_2 = ParkingLevel(spaces=[parking_space_c, parking_space_d])
    parking_level_3 = ParkingLevel(spaces=[parking_space_e, parking_space_f])

    garage = Garage(levels=[parking_level_1, parking_level_2, parking_level_3])

    vehicle_1 = Vehicle()
    vehicle_2 = Vehicle(vehicle_type=VehicleType.Compact, permit=Permit.DISABILITY)
    vehicle_3 = Vehicle(vehicle_type=VehicleType.Compact, permit=Permit.DISABILITY)
    vehicle_4 = Vehicle()
    vehicle_5 = Vehicle()
    vehicle_6 = Vehicle(vehicle_type=VehicleType.Compact, permit=Permit.DISABILITY)
    vehicle_7 = Vehicle(vehicle_type=VehicleType.Compact, permit=Permit.DISABILITY)

    expected_vehicles_on_level_1: List[Vehicle] = [vehicle_2, vehicle_7]
    expected_vehicles_on_level_2: List[Vehicle] = [None, vehicle_3]
    expected_vehicles_on_level_3: List[Vehicle] = [vehicle_6, None]

    garage.add_vehicles(
        [vehicle_1, vehicle_2, vehicle_3, vehicle_4, vehicle_5, vehicle_6, vehicle_7]
    )

    TestHelpers.assert_expected_parking_placement(
        levels=garage.levels,
        expected_levels=[
            expected_vehicles_on_level_1,
            expected_vehicles_on_level_2,
            expected_vehicles_on_level_3,
        ],
    )


def test_compact_vehicles_with_disability_permits_do_not_take_priority_over_non_permitted_spaces():
    parking_space_a = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_b = ParkingSpace(compact=True)
    parking_space_c = ParkingSpace(compact=True)
    parking_space_d = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_e = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_f = ParkingSpace(compact=True)

    parking_level_1 = ParkingLevel(spaces=[parking_space_a, parking_space_b])
    parking_level_2 = ParkingLevel(spaces=[parking_space_c, parking_space_d])
    parking_level_3 = ParkingLevel(spaces=[parking_space_e, parking_space_f])

    garage = Garage(levels=[parking_level_1, parking_level_2, parking_level_3])

    vehicle_1 = Vehicle()
    vehicle_2 = Vehicle(vehicle_type=VehicleType.Compact, permit=Permit.DISABILITY)
    vehicle_3 = Vehicle(vehicle_type=VehicleType.Compact, permit=Permit.DISABILITY)
    vehicle_4 = Vehicle(vehicle_type=VehicleType.Compact)
    vehicle_5 = Vehicle(vehicle_type=VehicleType.Compact)
    vehicle_6 = Vehicle(vehicle_type=VehicleType.Compact, permit=Permit.DISABILITY)
    vehicle_7 = Vehicle(vehicle_type=VehicleType.Compact, permit=Permit.DISABILITY)

    expected_vehicles_on_level_1: List[Vehicle] = [vehicle_2, vehicle_4]
    expected_vehicles_on_level_2: List[Vehicle] = [vehicle_5, vehicle_3]
    expected_vehicles_on_level_3: List[Vehicle] = [vehicle_6, vehicle_7]

    garage.add_vehicles(
        [vehicle_1, vehicle_2, vehicle_3, vehicle_4, vehicle_5, vehicle_6, vehicle_7]
    )

    TestHelpers.assert_expected_parking_placement(
        levels=garage.levels,
        expected_levels=[
            expected_vehicles_on_level_1,
            expected_vehicles_on_level_2,
            expected_vehicles_on_level_3,
        ],
    )

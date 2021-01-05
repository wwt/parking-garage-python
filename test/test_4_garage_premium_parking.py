from typing import List

from src.garage import Garage
from src.parking_level import ParkingLevel
from src.parking_space import ParkingSpace
from src.vehicle import Vehicle
from src.permit import Permit
from src.vehicle_type import VehicleType
from test_helpers.helpers import TestHelpers


def test_vehicles_without_premium_permits_are_rejected_from_premium_parking_spaces():
    parking_space_a = ParkingSpace(required_permit=Permit.PREMIUM)
    parking_space_b = ParkingSpace(required_permit=Permit.PREMIUM)
    parking_space_c = ParkingSpace(required_permit=Permit.PREMIUM)
    parking_space_d = ParkingSpace(required_permit=Permit.PREMIUM)
    parking_space_e = ParkingSpace(required_permit=Permit.PREMIUM)
    parking_space_f = ParkingSpace(required_permit=Permit.PREMIUM)

    parking_level_1 = ParkingLevel(spaces=[parking_space_a, parking_space_b])
    parking_level_2 = ParkingLevel(spaces=[parking_space_c, parking_space_d])
    parking_level_3 = ParkingLevel(spaces=[parking_space_e, parking_space_f])

    garage = Garage(levels=[parking_level_1, parking_level_2, parking_level_3])

    vehicle_1 = Vehicle(permit=Permit.PREMIUM)
    vehicle_2 = Vehicle(permit=Permit.NONE)
    vehicle_3 = Vehicle(permit=Permit.NONE)
    vehicle_4 = Vehicle(permit=Permit.PREMIUM)
    vehicle_5 = Vehicle(permit=Permit.DISABILITY)
    vehicle_6 = Vehicle(permit=Permit.NONE)

    expected_vehicles_rejected: List[Vehicle] = [
        vehicle_2,
        vehicle_3,
        vehicle_5,
        vehicle_6,
    ]

    actual_vehicles_rejected = garage.add_vehicles(
        [vehicle_1, vehicle_2, vehicle_3, vehicle_4, vehicle_5, vehicle_6]
    )

    TestHelpers.assert_expected_vehicles_are_rejected(
        actual=actual_vehicles_rejected, expected=expected_vehicles_rejected
    )


def test_vehicles_with_premium_permits_are_added_to_premium_parking_spaces():
    parking_space_a = ParkingSpace(required_permit=Permit.PREMIUM)
    parking_space_b = ParkingSpace()
    parking_space_c = ParkingSpace(required_permit=Permit.PREMIUM)
    parking_space_d = ParkingSpace(required_permit=Permit.PREMIUM)
    parking_space_e = ParkingSpace()
    parking_space_f = ParkingSpace(required_permit=Permit.PREMIUM)

    parking_level_1 = ParkingLevel(spaces=[parking_space_a, parking_space_b])
    parking_level_2 = ParkingLevel(spaces=[parking_space_c, parking_space_d])
    parking_level_3 = ParkingLevel(spaces=[parking_space_e, parking_space_f])

    garage = Garage(levels=[parking_level_1, parking_level_2, parking_level_3])

    vehicle_1 = Vehicle()
    vehicle_2 = Vehicle(permit=Permit.DISABILITY | Permit.PREMIUM)
    vehicle_3 = Vehicle(permit=Permit.PREMIUM)
    vehicle_4 = Vehicle()
    vehicle_5 = Vehicle()
    vehicle_6 = Vehicle(permit=Permit.PREMIUM)

    expected_vehicles_on_level_1: List[Vehicle] = [vehicle_2, vehicle_1]
    expected_vehicles_on_level_2: List[Vehicle] = [vehicle_3, vehicle_6]
    expected_vehicles_on_level_3: List[Vehicle] = [vehicle_4, None]

    garage.add_vehicles(
        [vehicle_1, vehicle_2, vehicle_3, vehicle_4, vehicle_5, vehicle_6]
    )

    TestHelpers.assert_expected_vehicles_on_levels(
        levels=garage.levels,
        expected_vehicles=[
            expected_vehicles_on_level_1,
            expected_vehicles_on_level_2,
            expected_vehicles_on_level_3,
        ],
    )


def test_vehicles_with_premium_permits_take_priority_over_non_permitted_spaces():
    parking_space_a = ParkingSpace(required_permit=Permit.PREMIUM)
    parking_space_b = ParkingSpace()
    parking_space_c = ParkingSpace()
    parking_space_d = ParkingSpace(required_permit=Permit.PREMIUM)
    parking_space_e = ParkingSpace()
    parking_space_f = ParkingSpace()

    parking_level_1 = ParkingLevel(spaces=[parking_space_a, parking_space_b])
    parking_level_2 = ParkingLevel(spaces=[parking_space_c, parking_space_d])
    parking_level_3 = ParkingLevel(spaces=[parking_space_e, parking_space_f])

    garage = Garage(levels=[parking_level_1, parking_level_2, parking_level_3])

    vehicle_1 = Vehicle()
    vehicle_2 = Vehicle(permit=Permit.PREMIUM)
    vehicle_3 = Vehicle(permit=Permit.PREMIUM)
    vehicle_4 = Vehicle()
    vehicle_5 = Vehicle(permit=Permit.PREMIUM)
    vehicle_6 = Vehicle(permit=Permit.PREMIUM)
    vehicle_7 = Vehicle(permit=Permit.PREMIUM)

    expected_vehicles_on_level_1: List[Vehicle] = [vehicle_2, vehicle_5]
    expected_vehicles_on_level_2: List[Vehicle] = [vehicle_6, vehicle_3]
    expected_vehicles_on_level_3: List[Vehicle] = [vehicle_7, vehicle_1]

    garage.add_vehicles(
        [vehicle_1, vehicle_2, vehicle_3, vehicle_4, vehicle_5, vehicle_6, vehicle_7]
    )

    TestHelpers.assert_expected_vehicles_on_levels(
        levels=garage.levels,
        expected_vehicles=[
            expected_vehicles_on_level_1,
            expected_vehicles_on_level_2,
            expected_vehicles_on_level_3,
        ],
    )


def test_vehicles_with_dual_premium_disability_permits_take_priority_over_premium_permitted_spaces():
    parking_space_a = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_b = ParkingSpace(required_permit=Permit.PREMIUM)
    parking_space_c = ParkingSpace(required_permit=Permit.PREMIUM)
    parking_space_d = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_e = ParkingSpace(required_permit=Permit.PREMIUM)
    parking_space_f = ParkingSpace(required_permit=Permit.PREMIUM)

    parking_level_1 = ParkingLevel(spaces=[parking_space_a, parking_space_b])
    parking_level_2 = ParkingLevel(spaces=[parking_space_c, parking_space_d])
    parking_level_3 = ParkingLevel(spaces=[parking_space_e, parking_space_f])

    garage = Garage(levels=[parking_level_1, parking_level_2, parking_level_3])

    vehicle_1 = Vehicle(permit=Permit.PREMIUM)
    vehicle_2 = Vehicle(permit=Permit.DISABILITY | Permit.PREMIUM)
    vehicle_3 = Vehicle(permit=Permit.DISABILITY | Permit.PREMIUM)
    vehicle_4 = Vehicle(permit=Permit.PREMIUM)
    vehicle_5 = Vehicle(permit=Permit.DISABILITY | Permit.PREMIUM)
    vehicle_6 = Vehicle(permit=Permit.DISABILITY | Permit.PREMIUM)

    expected_vehicles_on_level_1: List[Vehicle] = [vehicle_2, vehicle_5]
    expected_vehicles_on_level_2: List[Vehicle] = [vehicle_6, vehicle_3]
    expected_vehicles_on_level_3: List[Vehicle] = [vehicle_1, vehicle_4]

    garage.add_vehicles(
        [vehicle_1, vehicle_2, vehicle_3, vehicle_4, vehicle_5, vehicle_6]
    )

    TestHelpers.assert_expected_vehicles_on_levels(
        levels=garage.levels,
        expected_vehicles=[
            expected_vehicles_on_level_1,
            expected_vehicles_on_level_2,
            expected_vehicles_on_level_3,
        ],
    )


def test_compact_vehicles_with_premium_permits_are_prioritized_into_premium_parking_spaces():
    parking_space_a = ParkingSpace(required_permit=Permit.PREMIUM)
    parking_space_b = ParkingSpace(compact=True)
    parking_space_c = ParkingSpace(compact=True)
    parking_space_d = ParkingSpace(required_permit=Permit.PREMIUM)
    parking_space_e = ParkingSpace(required_permit=Permit.PREMIUM)
    parking_space_f = ParkingSpace(compact=True)

    parking_level_1 = ParkingLevel(spaces=[parking_space_a, parking_space_b])
    parking_level_2 = ParkingLevel(spaces=[parking_space_c, parking_space_d])
    parking_level_3 = ParkingLevel(spaces=[parking_space_e, parking_space_f])

    garage = Garage(levels=[parking_level_1, parking_level_2, parking_level_3])

    vehicle_1 = Vehicle()
    vehicle_2 = Vehicle(vehicle_type=VehicleType.Compact, permit=Permit.PREMIUM)
    vehicle_3 = Vehicle(vehicle_type=VehicleType.Compact, permit=Permit.PREMIUM)
    vehicle_4 = Vehicle()
    vehicle_5 = Vehicle()
    vehicle_6 = Vehicle(vehicle_type=VehicleType.Compact, permit=Permit.PREMIUM)
    vehicle_7 = Vehicle(vehicle_type=VehicleType.Compact, permit=Permit.PREMIUM)

    expected_vehicles_on_level_1: List[Vehicle] = [vehicle_2, vehicle_7]
    expected_vehicles_on_level_2: List[Vehicle] = [None, vehicle_3]
    expected_vehicles_on_level_3: List[Vehicle] = [vehicle_6, None]

    garage.add_vehicles(
        [vehicle_1, vehicle_2, vehicle_3, vehicle_4, vehicle_5, vehicle_6, vehicle_7]
    )

    TestHelpers.assert_expected_vehicles_on_levels(
        levels=garage.levels,
        expected_vehicles=[
            expected_vehicles_on_level_1,
            expected_vehicles_on_level_2,
            expected_vehicles_on_level_3,
        ],
    )


def test_compact_vehicles_with_dual_premium_disability_permits_take_the_same_priority_as_non_compact_vehicles():
    parking_space_a = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_b = ParkingSpace(required_permit=Permit.PREMIUM)
    parking_space_c = ParkingSpace(required_permit=Permit.PREMIUM)
    parking_space_d = ParkingSpace(required_permit=Permit.DISABILITY)
    parking_space_e = ParkingSpace(required_permit=Permit.PREMIUM)
    parking_space_f = ParkingSpace(required_permit=Permit.PREMIUM)

    parking_level_1 = ParkingLevel(spaces=[parking_space_a, parking_space_b])
    parking_level_2 = ParkingLevel(spaces=[parking_space_c, parking_space_d])
    parking_level_3 = ParkingLevel(spaces=[parking_space_e, parking_space_f])

    garage = Garage(levels=[parking_level_1, parking_level_2, parking_level_3])

    vehicle_1 = Vehicle(vehicle_type=VehicleType.Compact, permit=Permit.PREMIUM)
    vehicle_2 = Vehicle(
        vehicle_type=VehicleType.Truck, permit=Permit.DISABILITY | Permit.PREMIUM
    )
    vehicle_3 = Vehicle(
        vehicle_type=VehicleType.Compact, permit=Permit.DISABILITY | Permit.PREMIUM
    )
    vehicle_4 = Vehicle(vehicle_type=VehicleType.Compact, permit=Permit.PREMIUM)
    vehicle_5 = Vehicle(
        vehicle_type=VehicleType.Truck, permit=Permit.DISABILITY | Permit.PREMIUM
    )
    vehicle_6 = Vehicle(
        vehicle_type=VehicleType.Compact, permit=Permit.DISABILITY | Permit.PREMIUM
    )

    expected_vehicles_on_level_1: List[Vehicle] = [vehicle_2, vehicle_5]
    expected_vehicles_on_level_2: List[Vehicle] = [vehicle_6, vehicle_3]
    expected_vehicles_on_level_3: List[Vehicle] = [vehicle_1, vehicle_4]

    garage.add_vehicles(
        [vehicle_1, vehicle_2, vehicle_3, vehicle_4, vehicle_5, vehicle_6]
    )

    TestHelpers.assert_expected_vehicles_on_levels(
        levels=garage.levels,
        expected_vehicles=[
            expected_vehicles_on_level_1,
            expected_vehicles_on_level_2,
            expected_vehicles_on_level_3,
        ],
    )

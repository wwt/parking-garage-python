from typing import List

from src.garage import Garage
from src.parking_level import ParkingLevel
from src.parking_space import ParkingSpace
from src.vehicle import Vehicle
from src.permit import Permit
from src.vehicle_type import VehicleType
from test_helpers.helpers import TestHelpers


def test_new_vehicles_have_an_id():
    vehicle = Vehicle()

    assert isinstance(vehicle.vehicle_id, str)
    assert not vehicle.vehicle_id.isspace()


def test_new_vehicles_are_cars():
    vehicle = Vehicle()

    assert vehicle.vehicle_type is VehicleType.Car


def test_new_vehicles_do_not_have_permits():
    vehicle = Vehicle()

    assert vehicle.permit is Permit.NONE


def test_new_parking_spaces_are_not_compact():
    parking_space = ParkingSpace()

    assert not parking_space.compact


def test_new_parking_spaces_do_not_require_permits():
    parking_space = ParkingSpace()

    assert parking_space.required_permit is Permit.NONE


def test_new_parking_spaces_are_empty():
    parking_space = ParkingSpace()

    assert parking_space.vehicle is None


def test_new_garages_have_zero_levels():
    garage = Garage()

    assert len(garage.levels) == 0


def test_vehicle_is_added_to_parking_space():
    parking_space = ParkingSpace()
    parking_level = ParkingLevel(spaces=[parking_space])
    vehicle = Vehicle()

    garage = Garage(levels=[parking_level])
    garage.add_vehicles(vehicles=[vehicle])

    assert parking_space.vehicle is vehicle


def test_vehicles_are_added_to_single_level_garage_until_capacity_is_reached():
    parking_space_a = ParkingSpace()
    parking_space_b = ParkingSpace()
    parking_space_c = ParkingSpace()
    parking_space_d = ParkingSpace()
    parking_space_e = ParkingSpace()
    parking_space_f = ParkingSpace()

    parking_level_1 = ParkingLevel(
        spaces=[
            parking_space_a,
            parking_space_b,
            parking_space_c,
            parking_space_d,
            parking_space_e,
            parking_space_f,
        ]
    )

    garage = Garage(levels=[parking_level_1])

    vehicle_1 = Vehicle()
    vehicle_2 = Vehicle()
    vehicle_3 = Vehicle()
    vehicle_4 = Vehicle()
    vehicle_5 = Vehicle()
    vehicle_6 = Vehicle()
    vehicle_7 = Vehicle()

    expected_vehicles_on_level_1: List[Vehicle] = [
        vehicle_1,
        vehicle_2,
        vehicle_3,
        vehicle_4,
        vehicle_5,
        vehicle_6,
    ]

    garage.add_vehicles(
        [vehicle_1, vehicle_2, vehicle_3, vehicle_4, vehicle_5, vehicle_6, vehicle_7]
    )

    TestHelpers.assert_expected_vehicles_on_levels(
        levels=garage.levels,
        expected_vehicles=[
            expected_vehicles_on_level_1,
        ],
    )


def test_vehicles_are_added_to_multi_level_garage_until_capacity_is_reached():
    parking_space_a = ParkingSpace()
    parking_space_b = ParkingSpace()
    parking_space_c = ParkingSpace()
    parking_space_d = ParkingSpace()
    parking_space_e = ParkingSpace()
    parking_space_f = ParkingSpace()

    parking_level_1 = ParkingLevel(
        spaces=[parking_space_a, parking_space_b, parking_space_c]
    )
    parking_level_2 = ParkingLevel(spaces=[parking_space_d, parking_space_e])
    parking_level_3 = ParkingLevel(spaces=[parking_space_f])

    garage = Garage(levels=[parking_level_1, parking_level_2, parking_level_3])

    vehicle_1 = Vehicle()
    vehicle_2 = Vehicle()
    vehicle_3 = Vehicle()
    vehicle_4 = Vehicle()
    vehicle_5 = Vehicle()
    vehicle_6 = Vehicle()
    vehicle_7 = Vehicle()

    expected_vehicles_on_level_1: List[Vehicle] = [vehicle_1, vehicle_2, vehicle_3]
    expected_vehicles_on_level_2: List[Vehicle] = [vehicle_4, vehicle_5]
    expected_vehicles_on_level_3: List[Vehicle] = [vehicle_6]

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


def test_vehicles_are_rejected_when_capacity_is_exceeded():
    parking_space_a = ParkingSpace()
    parking_space_b = ParkingSpace()
    parking_space_c = ParkingSpace()

    parking_level_1 = ParkingLevel(spaces=[parking_space_a, parking_space_b])
    parking_level_2 = ParkingLevel(spaces=[parking_space_c])

    garage = Garage(levels=[parking_level_1, parking_level_2])

    vehicle_1 = Vehicle()
    vehicle_2 = Vehicle()
    vehicle_3 = Vehicle()
    vehicle_4 = Vehicle()
    vehicle_5 = Vehicle()
    vehicle_6 = Vehicle()
    vehicle_7 = Vehicle()

    expected_vehicles_rejected: List[Vehicle] = [
        vehicle_4,
        vehicle_5,
        vehicle_6,
        vehicle_7,
    ]

    actual_vehicles_rejected = garage.add_vehicles(
        [vehicle_1, vehicle_2, vehicle_3, vehicle_4, vehicle_5, vehicle_6, vehicle_7]
    )

    TestHelpers.assert_expected_vehicles_are_rejected(
        actual=actual_vehicles_rejected, expected=expected_vehicles_rejected
    )

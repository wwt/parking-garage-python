from typing import List

from garage.garage import Garage
from garage.parking_level import ParkingLevel
from garage.vehicle import Vehicle


class TestHelpers:
    @staticmethod
    def garage_vehicles(garage: Garage) -> List[Vehicle]:
        return [
            space.vehicle
            for level in garage.levels
            for space in level.spaces
            if isinstance(space.vehicle, Vehicle)
        ]

    @staticmethod
    def garage_capacity(garage: Garage) -> int:
        return len(
            [
                space
                for level in garage.levels
                if level.spaces is not None
                for space in level.spaces
                if space is not None
            ]
        )

    @staticmethod
    def garage_occupancy(garage: Garage) -> int:
        return len(
            [
                space.vehicle
                for level in garage.levels
                if level.spaces is not None
                for space in level.spaces
                if isinstance(space.vehicle, Vehicle)
            ]
        )

    @staticmethod
    def vehicles_on_level(level: ParkingLevel) -> List[Vehicle]:
        return [space.vehicle for space in level.spaces]

    @staticmethod
    def level_capacity(level: ParkingLevel) -> int:
        return len(level.spaces)

    @staticmethod
    def level_occupancy(level: ParkingLevel) -> int:
        return len(
            [
                space.vehicle
                for space in level.spaces
                if isinstance(space.vehicle, Vehicle)
            ]
        )

    @staticmethod
    def assert_expected_parking_placement(
        levels: List[ParkingLevel], expected_levels: List[List[Vehicle]]
    ):
        assert len(levels) == len(expected_levels)

        for index, parking_level in enumerate(levels):
            assert all(
                [
                    actual is expected
                    for actual, expected in zip(
                        TestHelpers.vehicles_on_level(level=parking_level),
                        expected_levels[index],
                    )
                ]
            ), "Vehicle was not found in the expected parking space."

    @staticmethod
    def assert_expected_vehicles_are_rejected(
        actual: List[Vehicle],
        expected: List[Vehicle],
    ):
        assert len(actual) == len(
            expected
        ), "Unexpected number of vehicles were rejected."
        assert all(
            [actual is expected for actual, expected in zip(actual, expected)]
        ), "Unexpected vehicle was rejected from the garage. Or an unexpected rejection order."

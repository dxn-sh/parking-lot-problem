from parking_lot import *


def test_parking_spot():
    spot1 = ParkingSpot(1, 2, 7)
    assert spot1.get_spot_id() == 7
    assert spot1.get_car() == ""

    spot1.park_car("6FOU3HY")
    assert spot1.get_car() == "6FOU3HY"

    spot1.remove_car()
    assert spot1.get_car() == ""


def test_floor():
    floor1 = Floor(1, 1, 5)
    assert floor1.floor_availability() == 5
    assert floor1.is_full() is False


def test_floor_park():
    floor1 = Floor(1, 1, 5)
    spot = ParkingSpot(1, 1, 1, "6FOU3HY")
    parking = floor1.park_car("6FOU3HY")
    assert parking.get_spot_id() == spot.get_spot_id()
    assert floor1.floor_availability() == 4


def test_floor_park_full():
    floor2 = Floor(1, 2, 2)
    floor2.park_car("6FOU3HY")
    floor2.park_car("AL909EQ")
    assert floor2.park_car("29MI7LL") is None
    assert floor2.floor_availability() == 0


def test_floor_remove():
    floor1 = Floor(1, 1, 5)
    spot1 = ParkingSpot(1, 1, 1, "6FOU3HY")
    spot2 = ParkingSpot(1, 1, 2, "AL909EQ")
    floor1.park_car("6FOU3HY")
    floor1.park_car("AL909EQ")
    floor1.park_car("29MI7LL")
    removed = floor1.remove_car("6FOU3HY")
    assert removed.get_spot_id() == spot1.get_spot_id()
    assert floor1.floor_availability() == 3

    removed = floor1.remove_car("AL909EQ")
    assert removed.get_spot_id() == spot2.get_spot_id()
    assert floor1.floor_availability() == 4

    # Check spot assigned in correct order
    parked = floor1.park_car("JTT856U")
    assert parked.get_spot_id() == spot1.get_spot_id()
    assert floor1.floor_availability() == 3


def test_lot():
    lot1 = ParkingLot(1, 2, 3)
    assert lot1.lot_availability() == 6


def test_lot_park():
    lot1 = ParkingLot(1, 2, 3)
    parked = lot1.park_car("6FOU3HY")
    assert parked == (f'License Plate: 6FOU3HY\n'
                      f'Lot 1 Floor 1 Parking Spot 1 --> OCCUPIED\n'
                      f'Spots Available on Floor 1: 2\n'
                      f'Spots Available in Lot 1: 5')

    parked = lot1.park_car("AL909EQ")
    assert parked == (f'License Plate: AL909EQ\n'
                      f'Lot 1 Floor 1 Parking Spot 2 --> OCCUPIED\n'
                      f'Spots Available on Floor 1: 1\n'
                      f'Spots Available in Lot 1: 4')


def test_lot_park_full():
    lot2 = ParkingLot(1, 2, 2)
    lot2.park_car("6FOU3HY")
    lot2.park_car("AL909EQ")
    lot2.park_car("29MI7LL")
    parked = lot2.park_car("JTT856U")
    assert parked == (f'License Plate: JTT856U\n'
                      f'Lot 1 Floor 2 Parking Spot 2 --> OCCUPIED\n'
                      f'Spots Available on Floor 2: 0\n'
                      f'Spots Available in Lot 1: 0')

    assert lot2.park_car("SCH4N76") == "Lot is full. No parking available."


def test_lot_remove():
    lot2 = ParkingLot(1, 2, 2)
    lot2.park_car("6FOU3HY")
    lot2.park_car("AL909EQ")
    lot2.park_car("29MI7LL")
    lot2.park_car("JTT856U")
    removed = lot2.remove_car("AL909EQ")
    assert removed == (f'License Plate: AL909EQ\n'
                       f'Lot 1 Floor 1 Parking Spot 2 --> VACATED\n'
                       f'Spots Available on Floor 1: 1\n'
                       f'Spots Available in Lot 1: 1')

    removed = lot2.remove_car("JTT856U")
    assert removed == (f'License Plate: JTT856U\n'
                       f'Lot 1 Floor 2 Parking Spot 2 --> VACATED\n'
                       f'Spots Available on Floor 2: 1\n'
                       f'Spots Available in Lot 1: 2')

    # Check spot assigned in correct order
    parked = lot2.park_car("SCH4N76")
    assert parked == (f'License Plate: SCH4N76\n'
                      f'Lot 1 Floor 1 Parking Spot 2 --> OCCUPIED\n'
                      f'Spots Available on Floor 1: 0\n'
                      f'Spots Available in Lot 1: 1')


def test_lot_remove_fail():
    lot1 = ParkingLot(1, 2, 3)
    assert lot1.remove_car("6FOU3HY") == "Car not identified."

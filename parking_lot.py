class ParkingSpot:
    # Constructor requires locations of parking lot, floor, and spot
    # If occupied, provide car license plate; default empty string
    def __init__(self, lot_id: int, floor_id: int, spot_id: int, car: str = ""):
        self.lot_id = lot_id
        self.floor_id = floor_id
        self.spot_id = spot_id
        self.car = car

    def park_car(self, car: str):
        self.car = car

    def remove_car(self):
        self.car = ""

    def get_spot_id(self):
        return self.spot_id

    def get_spot_floor(self):
        return self.floor_id

    def get_car(self):
        return self.car


class Floor:
    def __init__(self, lot_id: int, floor_id: int, num_spots: int):
        self.lot_id = lot_id
        self.floor_id = floor_id
        self.spots = num_spots
        self.available = []
        self.taken = []

        # Add available parking spots
        for i in range(1, num_spots + 1, 1):
            self.available.append(ParkingSpot(self.lot_id, self.floor_id, i))

    # Determine a parking spot for a given car
    def park_car(self, car: str):
        if not self.is_full():
            location = self.available.pop(0)
            location.park_car(car)
            self.taken.append(location)
            return location
        return None

    # Make parking spot available when given car leaves
    def remove_car(self, car: str):
        removed = None

        # Of all taken parking spots, search for given car to remove
        for location in self.taken:
            if location.get_car() == car:
                location.remove_car()
                self.taken.remove(location)
                self.available.insert(0, location)
                removed = location
                break

        # If car successfully located in floor
        if removed is not None:
            # Ensure available spots ordered from closest to farthest
            # i.e. least to greatest spot id
            x = 0
            while (len(self.available) >= 2
                    and x <= len(self.available) - 1
                   and self.available[x].get_spot_id() > self.available[x + 1].get_spot_id()):
                self.available[x], self.available[x + 1] = self.available[x + 1], self.available[x]
                x += 1

            return removed
        else:
            return None

    def floor_availability(self):
        return len(self.available)

    # Return True if all spots on floor are taken; else False
    def is_full(self):
        if len(self.taken) == self.spots:
            return True
        else:
            return False


class ParkingLot:
    def __init__(self, lot_id: int, num_floors: int, num_spots: int):
        self.lot_id = lot_id
        self.floors = []
        self.size = num_floors * num_spots

        # Add floor in a lot
        for i in range(1, num_floors + 1, 1):
            self.floors.append(Floor(self.lot_id, i, num_spots))

    # Add car to lot and give updated parking spot availability
    def park_car(self, car: str):
        for curr_floor in self.floors:
            if not curr_floor.is_full():
                parked = curr_floor.park_car(car)
                return self.inventory(car, False, parked)
        return "Lot is full. No parking available."

    # Remove car from lot and give updated parking spot availability
    def remove_car(self, car: str):
        for curr_floor in self.floors:
            removed = curr_floor.remove_car(car)
            if removed is not None:
                return self.inventory(car, True, removed)
        return "Car not identified."

    def lot_availability(self):
        available = 0
        for curr_floor in self.floors:
            available += curr_floor.floor_availability()
        return available

    # Return the current availability for current lot and floor
    # Include id of spot recently occupied/vacated
    def inventory(self, car: str, available: bool, spot: ParkingSpot):
        curr_floor = spot.get_spot_floor()
        status = "OCCUPIED"
        if available:
            status = "VACATED"

        return (f'License Plate: {car}\n'
                f'Lot {self.lot_id} Floor {curr_floor} Parking Spot {spot.get_spot_id()} --> {status}\n'
                f'Spots Available on Floor {curr_floor}: {self.floors[curr_floor - 1].floor_availability()}\n'
                f'Spots Available in Lot {self.lot_id}: {self.lot_availability()}')

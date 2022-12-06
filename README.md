# parking lot problem

Create a parking lot such that a given parking lot can have "x" number of floors and each floor can have "y" number of spots. Every parking spot is given a unique identification. Each car is given a specific parking spot. Assuming a linear ordering of parking spots, the assigned parking spot should be the closest available spot to the entrance.

<br>

### Code
Parking lot implementation available [here](https://github.com/dxn-sh/parking-lot-problem/blob/main/parking_lot.py).

**ParkingSpot**: A class to represent a parking spot. Constructor requires numerical identification of lot, floor, and spot. If parking spot is occupied, provide the car license plate.

**Floor**: A class to represent a floor of a parking lot. Constructor will create an array of ParkingSpots available and ParkingSpots taken given the number of total parking spots on a floor.

**ParkingLot**: A class to represent a parking lot. Constructor will create an array of Floors given the number of total floors and total parking spots per floor. Each floor assumed to have the same number of parking spots.

<br>

### Tests
Testing with pytest of parking lot implementation available [here](https://github.com/dxn-sh/parking-lot-problem/blob/main/parking_lot_test.py). Includes testing of:
- Constructors of each class
- park_car() and remove_car() for each class
- floor_availability() and lot_availability()
- Adding and removing multiple cars
- Adding to full floor and full lot
- Removing car that is not there
- Adding a car after removing cars to ensure correct order of available spots

<br>

### Other Considerations
- Optimizing removing a car: (1) change the current data structure used (array) to a set or hashmap or (2) implement a ticketing system to directly obtain the location of the parking spot a car was at 
- Is there only one entrance and exit per parking lot? Per floor? If not can more than one car enter or exit at a time? How would this affect assigning parking spots?
- Is there one standard parking spot size for cars or are there spots available for compact vehicles, motorcycles, trucks, etc.?

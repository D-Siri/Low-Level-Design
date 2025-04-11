from parking_lot import ParkingLot
from vehicle_types import Vehicle
from vehicles import Car, Motorcycles, Trucks
parking_lot = ParkingLot()
parking_lot.add_level(Vehicle.CAR, 10)
parking_lot.add_level(Vehicle.TRUCK, 20)
parking_lot.add_level(Vehicle.MOTORCYCLE, 20)

car = Car("ABC123")
truck = Trucks("XYZ789")
motorcycle = Motorcycles("M1234")

parking_lot.park_vehicle(car)
parking_lot.park_vehicle(truck)
parking_lot.park_vehicle(motorcycle)

parking_lot.show_available_slots(Vehicle.MOTORCYCLE)

# Un park vehicle
parking_lot.exit_vehicle(motorcycle)

# Display updated availability
parking_lot.show_available_slots(Vehicle.MOTORCYCLE)

class Spot:
    def __init__(self, slot_id):
        self.vehicle = None
        self.available = True
        self.slot_id = slot_id

    def __str__(self):
        return str(self.slot_id)

    def park_vehicle(self, vehicle):
        if not self.available:
            return False
        self.vehicle = vehicle
        self.available = False
        print(f"{vehicle.plate_number} Parked")
        return True

    def exit_vehicle(self, vehicle):
        if self.vehicle == vehicle:
            self.vehicle = None
            print(f"{vehicle.plate_number} left the parking lot")
            self.available = True
            return True
        return False

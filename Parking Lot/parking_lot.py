from levels import Levels


class ParkingLot:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.levels = []
            cls.initialized = False
        return cls.instance

    def add_level(self, type, n_spots):
        id = len(self.levels) + 1
        self.levels.append(Levels(id, type, n_spots))

    def park_vehicle(self, vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

    def exit_vehicle(self, vehicle):
        for level in self.levels:
            if level.exit_vehicle(vehicle):
                return True
        return False

    def show_available_slots(self, vehicle):
        for level in self.levels:
            level.show_available_slots(vehicle)

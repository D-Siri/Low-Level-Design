from spot import Spot


class Levels:

    def __init__(self, level_id, type, n_spots=20):
        self.level_id = level_id
        self.spots = [Spot(str(level_id) + "-" + str(i)) for i in range(n_spots)]
        self.type = type

    def park_vehicle(self, vehicle):

        if vehicle.get_type() != self.type:
            return False

        for s in self.spots:
            if s.park_vehicle(vehicle):
                return True

        return False

    def exit_vehicle(self, vehicle):
        for s in self.spots:
            if s.exit_vehicle(vehicle):
                return True

        return False

    def show_available_slots(self, vehicle):
        if vehicle == self.type:
            for s in self.spots:
                if s.available:
                    print(s)

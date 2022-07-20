class Tires:
    def __init__(self, size):
        self.size = size

    def get_pressure(self):
        pass


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def start(self):
        pass

    def stop(self):
        pass

    def get_state(self):
        pass


class Vehicle:
    def __init__(self, vin, engine, tires):
        self.VIN = vin
        self.engine = engine
        self.tires = tires


if __name__ == '__main__':
    def main():
        city_tires = Tires(size=15)
        off_road_tires = Tires(size=18)

        electric_engine = Engine(fuel_type='electricity')
        petrol_engine = Engine(fuel_type='petroleum')

        city_car = Vehicle(vin=1, engine=electric_engine, tires=city_tires)
        all_terrain_car = Vehicle(vin=2, engine=petrol_engine, tires=off_road_tires)

    main()
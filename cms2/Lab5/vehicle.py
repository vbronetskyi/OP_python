"""Lab.5_task.3"""


class Vehicle:
    """class Vehicle"""

    def __init__(
        self,
        brand,
        model,
        type,
        tank_volume,
        fuel_per_hundred_km=6,
        amount_of_fuel_filled=0,
    ) -> None:
        self.brand = brand
        self.model = model
        self.type = type
        self.tank_volume = tank_volume
        self.fuel_per_hundred_km = fuel_per_hundred_km
        self.amount_of_fuel_filled = amount_of_fuel_filled

    def __repr__(self) -> str:  # ("Subaru", "Forester", "Crossover", 16, 7)
        """Work"""
        return f"Vehicle {self.brand} {self.model} is a {self.type}. It has a gas tank size \
of {self.tank_volume}."

    def fuel_up(self, fuel):
        """fuel_up"""
        self.amount_of_fuel_filled += fuel
        if self.amount_of_fuel_filled >= 12:
            return "Gas tank is filled."

    def get_fuel_level(self):
        """get_fuel_level"""
        return self.amount_of_fuel_filled

    def drive(self, km_to_drive):
        """drive"""
        if (
            self.amount_of_fuel_filled - self.fuel_per_hundred_km * km_to_drive / 100
            < 0
        ):
            return "Not enough fuel level in a gas tank."
        self.amount_of_fuel_filled -= self.fuel_per_hundred_km * km_to_drive / 100
        return "The Subaru Forester is now driving."


class Battery:
    """class Battery"""

    def __init__(self, battery_size, charge_level) -> None:
        """constructor"""
        self.battery_size = battery_size
        self.charge_level = charge_level


class ElectricVehicle(Vehicle, Battery):
    """class ElectricVehicle"""

    def __init__(self, brand, model, type) -> None:
        Vehicle.__init__(
            self,
            brand,
            model,
            type,
            tank_volume=None,
            fuel_per_hundred_km=None,
            amount_of_fuel_filled=0,
        )
        self.battery = Battery(battery_size=85, charge_level=0)

    def __repr__(self) -> str:
        return f"Vehicle {self.brand} {self.model} is a {self.type}."

    def charge(self):
        """charge Vehicle"""
        self.battery.charge_level = 100
        return "The vehicle is fully charged."

    def get_charge_level(self):
        """return charge level"""
        return self.battery.charge_level

    def drive(self, km_to_drive=100):
        """drive the car """
        #for 100 km 20% charge_level
        self.battery.charge_level -=km_to_drive/100*20
        return "The Tesla Model 3 is now driving."

    def get_battery_info(self):
        return f"Battery has size of {self.battery.battery_size}, it is charged \
up to {self.battery.charge_level}%"


def test_vehicle():
    """
    Test function
    """
    print("Testing Vehicle classes...")
    # A basic Vehicle has a brand, model, type, volume of gas_tank_size
    # fuel_consumption that by default equals 6 and fuel_level that by default equals 0.
    #It can drive and be fueled up
    vehicle = Vehicle("Subaru", "Forester", "Crossover", 16, 7)
    assert (type(vehicle) == Vehicle)
    assert (isinstance(vehicle, Vehicle))
    assert (str(vehicle) == "Vehicle Subaru Forester is a Crossover. It has a gas tank size of 16.")

    # change some attributes
    assert (vehicle.fuel_up(12) == "Gas tank is filled.")
    assert (vehicle.get_fuel_level() == 12)
    # When vehicle drives, it uses the fuel level
    # Vehicle uses fuel in amount of
    # fuel_consumption * distance to drive / 100
    assert (vehicle.drive(100) == "The Subaru Forester is now driving.")
    # the vehicle travelled 100 km and the fuel level reduced
    # from 12 to 5
    assert (vehicle.get_fuel_level() == 5)
    assert (vehicle.drive(100) == "Not enough fuel level in a gas tank.")

    # ElectricVehicle is a Vehicle that doesn't need a gas_tank_size
    # and doesn't have a fuel_consumption.
    # Instead it has energy consumption of your battery charge for 100 km.
    # It is calculated as battery_consumption * distance to drive / 100
    # By default that battery_consumption equals to 20
    # You can charge and drive it.
    electric_vehicle = ElectricVehicle('Tesla', 'Model 3', 'Sedan')
    assert (type(electric_vehicle) == ElectricVehicle)
    assert (isinstance(electric_vehicle, ElectricVehicle))
    assert (isinstance(electric_vehicle, Vehicle))
    assert (str(electric_vehicle) == "Vehicle Tesla Model 3 is a Sedan.")

    # the attribute battery has to belong to Battery class
    # the Battery has a size, that by default equals 85
    # and charge level that by default equals 0
    assert (type(electric_vehicle.battery) == Battery)
    assert (isinstance(electric_vehicle.battery, Battery))
    assert (electric_vehicle.get_battery_info() == "Battery has size of 85, it is charged up to 0%")

    assert (electric_vehicle.get_fuel_level() == 0)
    assert (electric_vehicle.charge() == "The vehicle is fully charged.")
    assert (electric_vehicle.get_charge_level() == 100)
    assert (electric_vehicle.drive(200) == "The Tesla Model 3 is now driving.")
    assert (electric_vehicle.get_charge_level() == 60)

    print("Done!")


if __name__ == '__main__':
    test_vehicle()

from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass

def add_years_to_date(original_date, years_to_add):
    result = original_date.replace(year=original_date.year + years_to_add)
    return result

class Tires(ABC):
    def needs_service(self):
        pass

class CarriganTires(Tires):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        for tire in self.wear:
            if tire >= 0.9:
                return True
        return False

class OctoprimeTires(Tires):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        return sum(self.wear) >= 3.0

class Battery(ABC):
    def needs_service(self):
        pass

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        date_which_battery_should_be_serviced_by = add_years_to_date(self.last_service_date, 4)
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        date_which_battery_should_be_serviced_by = add_years_to_date(self.last_service_date, 3)
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False

class Engine(ABC):
    def needs_service(self):
        pass

class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False

class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000

class WilloughbyEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000

class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car


import unittest
from datetime import datetime

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2016-01-25")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2018-01-25")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = CapuletEngine(30001, 0)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = CapuletEngine(30000, 0)
        self.assertFalse(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = WilloughbyEngine(60001, 0)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = WilloughbyEngine(60000, 0)
        self.assertFalse(engine.needs_service())

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        wear = [0.1, 0.3, 0.2, 0.9]
        tires = CarriganTires(wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        wear = [0.1, 0.2, 0.4, 0.2]
        tires = CarriganTires(wear)
        self.assertFalse(tires.needs_service())

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        wear = [0.8, 0.8, 0.8, 0.7]
        tires = OctoprimeTires(wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        wear = [0.1, 0.2, 0.4, 0.2]
        tires = OctoprimeTires(wear)
        self.assertFalse(tires.needs_service())
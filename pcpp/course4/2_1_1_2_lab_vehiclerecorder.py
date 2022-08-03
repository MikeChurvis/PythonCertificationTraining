from __future__ import annotations
import json
from dataclasses import dataclass


@dataclass(frozen=True)
class Vehicle:
    registration_number: str
    year_of_production: int
    passenger: bool
    mass: float

    @classmethod
    def from_standard_input(cls) -> Vehicle:
        while True:
            registration_number = input("Registration number: ").strip().upper()
            try:
                if len(registration_number) not in range(6, 9):
                    raise ValueError
            except ValueError:
                print(f"\tERROR: Registration number must be 6, 7, or 8 characters long "
                      f"(the value you gave was {len(registration_number)} long).")
            else:
                break

        while True:
            year_of_production = input("Year of production: ").strip()
            try:
                year_of_production = int(year_of_production)
                if year_of_production not in range(10000):
                    raise ValueError
            except (TypeError, ValueError):
                print(f"\tERROR: {year_of_production} is an invalid value for year of production "
                      f"(must be an integer between 0 and 9999 inclusive).")
            else:
                break

        while True:
            passenger = input("Passenger [y/n]: ").strip().lower()
            try:
                if passenger not in 'yn':
                    raise ValueError
                passenger = True if passenger == 'y' else False
            except ValueError:
                print(f"\tERROR: {passenger} is an invalid value for passenger (must enter y for YES or n for NO).")
            else:
                break

        while True:
            mass = input("Vehicle mass (kg): ").strip()
            try:
                mass = float(mass)
                if mass <= 0:
                    raise ValueError
            except (TypeError, ValueError):
                print(f"\tERROR: {mass} is an invalid value for vehicle mass (must be a number greater than zero).")
            else:
                break

        return cls(registration_number, year_of_production, passenger, mass)

    @classmethod
    def from_json(cls, json_string: str) -> Vehicle:
        return Vehicle(**json.loads(json_string))

    def to_json(self) -> str:
        return json.dumps(self.__dict__)


def prompt_user__main_menu():
    options = {
        "1": ("produce a JSON string describing a vehicle", prompt_user__enter_car_data_then_print_json),
        "2": ("decode a JSON string into vehicle data", prompt_user__enter_json_then_show_car_data_repr),
    }
    print("What can I do for you?")

    while True:
        for opt_key in options:
            opt_label = options[opt_key][0]
            print(f"{opt_key} - {opt_label}")

        user_choice = input("Your choice: ").strip()

        if user_choice not in options:
            print(f"\tERROR: '{user_choice}' is not a valid choice. "
                  f"Please select from the options below, or press Ctrl+C to exit: ")
            continue
        break

    # Invoke the function corresponding to the user's choice.
    options[user_choice][1]()


def prompt_user__enter_json_then_show_car_data_repr():
    while True:
        car_data = input("Enter vehicle JSON string (or Ctrl+C to exit): ").strip()
        try:
            print(Vehicle.from_json(car_data))
        except json.JSONDecodeError:
            print("The given string is not valid JSON data.")
        except TypeError as error:
            print(f"One or more values provided were of an unexpected type. Details below:\n\n{error}")
        else:
            break


def prompt_user__enter_car_data_then_print_json():
    vehicle = Vehicle.from_standard_input()
    print(f"Resulting JSON string is:\n{vehicle.to_json()}")


if __name__ == '__main__':
    def main():
        prompt_user__main_menu()


    main()

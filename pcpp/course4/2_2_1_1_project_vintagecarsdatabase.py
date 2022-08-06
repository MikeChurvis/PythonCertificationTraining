"""
Below are a set of terminal output frames that demonstrate the behavior of this app from the
perspective of the end-user.

+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 1
*** Database is empty ***

+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 2
Car ID (empty string to exit): 1
Car brand (empty string to exit): Porsche
Car model (empty string to exit): 911
Car production year (empty string to exit): 1963
Is this car convertible? [y/n] (empty string to exit): n

+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 2
Car ID (empty string to exit): 2
Car brand (empty string to exit): Ford
Car model (empty string to exit): Mustang
Car production year (empty string to exit): 1972
Is this car convertible? [y/n] (empty string to exit): y

+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 1
id        | brand          | model     | production_year     | convertible    |
1         | Porsche        | 911       | 1963                | False          |
2         | Ford           | Mustang   | 1972                | True           |

+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4):  4
Car ID (empty string to exit): 2
Car brand (empty string to exit): Ford
Car model (empty string to exit): Mustang
Car production year (empty string to exit): 1973
Is this car convertible? [y/n] (empty string to exit): n

+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 3
Car ID (empty string to exit): 1
Success!
Car ID (empty string to exit):

+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 0
Bye!
"""
from __future__ import annotations

import dataclasses
import re

import requests
import json


@dataclasses.dataclass(frozen=True)
class VintageCar:
    id: int
    model: str
    brand: str
    production_year: int
    convertible: bool

    class InvalidDataError(ValueError):
        pass

    def validate(self):
        """
        Validates the current instance's data. If everything is OK then nothing happens, otherwise an error is raised.
        Intended to be called from the .__post_init__ method.

        :return: None
        :raises VintageCar.InvalidDataError: if any data validity check fails.
        """
        # Validate ID.
        if not isinstance(self.id, int):
            raise VintageCar.InvalidDataError(
                f"VintageCar.id must be an integer. The value given was {self.id} which is of type {type(self.id)}."
            )

        if not self.id >= 0:
            raise VintageCar.InvalidDataError(
                f"VintageCar.id must be non-negative. The value given was {self.id}."
            )

        # Validate model and brand.
        def validate_character_field(field_name, value):
            if not isinstance(value, str):
                raise VintageCar.InvalidDataError(
                    f"VintageCar.{field_name} must be a string. The value given was {value} of type {type(value)}."
                )

            if len(value) == 0:
                raise VintageCar.InvalidDataError(
                    f"VintageCar.{field_name} must contain at least one character. "
                    f"The value given was an empty string.")

            if re.search(r'[^a-zA-Z\d ]', value) is not None:
                raise VintageCar.InvalidDataError(
                    f"VintageCar.{field_name} may only contain letters, numbers, and spaces. "
                    f"The value given was {value}."
                )

        validate_character_field('model', self.model)
        validate_character_field('brand', self.brand)

        # Validate production year.
        if not isinstance(self.production_year, int):
            raise VintageCar.InvalidDataError(
                f"VintageCar.production_year must be an integer. "
                f"The value given was {self.production_year} which is of type {type(self.production_year)}."
            )

        if self.production_year < 1900:
            raise VintageCar.InvalidDataError(
                f"VintageCar.production_year must be at least 1900. The value given was {self.production_year}."
            )

        if self.production_year >= 2000:
            raise VintageCar.InvalidDataError(
                f"VintageCar.production_year must be earlier than 2000. The value given was {self.production_year}."
            )

        # Validate convertible status.
        if not isinstance(self.convertible, bool):
            raise VintageCar.InvalidDataError(
                f"VintageCar.convertible must be a boolean value. The value given was {self.convertible} "
                f"which is of type {type(self.convertible)}."
            )

    def __post_init__(self):
        self.validate()

    @classmethod
    def from_dict(cls, d: dict) -> VintageCar:
        return cls(**d)


class VintageCarsAPIService:
    rest_api_root_url = 'http://localhost:3000/vintage_cars'

    class APIServerError(ConnectionError):
        pass

    class InvalidOperationError(Exception):
        pass

    def __init__(self):
        """
        Provides a high-level API for interacting with the Vintage Cars Database.
        Persists a Session object to avoid the `requests` library's notorious slowdowns.
        """
        self.__session = requests.Session()
        self.__next_available_id = None

        try:
            server_response = self.__session.head(self.rest_api_root_url)
            if not server_response.ok:
                raise VintageCarsAPIService.APIServerError(
                    f"The server responded with a non-OK status ({server_response.status_code}).")
        except (requests.exceptions.RequestException, VintageCarsAPIService.APIServerError) as error:
            print_fatal_error_and_exit(
                f"A {type(error).__name__} was raised while trying to connect to the Vintage Cars Database",
                detail=error
            )
            exit(1)

        self.__next_available_id = self.__session.get(f"{self.rest_api_root_url}_meta").json().get('next_id')
        print(self.__next_available_id)

    def get_list_of_all_vintage_cars(self) -> list[VintageCar]:
        """

        :return: A list of all vintage cars in the database, represented by VintageCar objects.
        """
        try:
            data = self.__session.get(self.rest_api_root_url).json(object_hook=VintageCar.from_dict)
        except VintageCar.InvalidDataError as error:
            print_fatal_error_and_exit(
                "The server responded with JSON data that cannot be converted into a valid VintageCar object",
                detail=error
            )
        else:
            return data

    def check_if_vintage_car_is_in_db(self, vintage_car_id: int):
        return self.__session.head(f"{self.rest_api_root_url}/{vintage_car_id}").ok

    def get_next_available_id(self):
        self.__next_available_id = self.__session.get(f"{self.rest_api_root_url}_meta").json().get('next_id')
        return self.__next_available_id

    def increment_next_available_id(self):
        self.__next_available_id = self.get_next_available_id() + 1
        self.__session.post(f"{self.rest_api_root_url}_meta", params={"next_id": self.__next_available_id})

    def add_vintage_car_to_database(self, vintage_car_data: VintageCar | dict):
        if isinstance(vintage_car_data, dict):
            try:
                vintage_car_data = VintageCar(**vintage_car_data)
            except VintageCar.InvalidDataError as error:
                raise VintageCarsAPIService.InvalidOperationError(
                    "[ERROR] Cannot add new vintage car to database."
                    "\n\tReason: the car data dictionary given can not be converted into a valid VintageCar object."
                    f"\n\tDetail: {str(error)}"
                )

        id_exists_in_db = self.check_if_vintage_car_is_in_db(vintage_car_data.id)





def print_fatal_error_and_exit(message, *, detail, exit_code=1):
    print(f"[FATAL ERROR] {str(message)}"
          f"\n\tDetail: {str(detail)}"
          f"\n\tThe program will now close.")
    exit(exit_code)


if __name__ == '__main__':
    def main():
        service = VintageCarsAPIService()
        print(service.check_if_vintage_car_is_in_db(0))
        print(service.check_if_vintage_car_is_in_db(1))


    main()

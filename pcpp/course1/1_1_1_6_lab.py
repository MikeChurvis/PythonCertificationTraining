"""
Scenario

- create a class representing a mobile phone;
- your class should implement the following methods:

    - `__init__` expects a number to be passed as an argument; this method stores the number in an instance variable
      `self.number`
    - `turn_on()` should return the message 'mobile phone {number} is turned on'.
      Curly brackets are used to mark the place to insert the object's number variable;
    - `turn_off()` should return the message 'mobile phone is turned off';
    - `call(number)` should return the message 'calling {number}'. Curly brackets are used to mark the place to insert
      the object's number variable;

- create two objects representing two different mobile phones; assign any random phone numbers to them;
- implement a sequence of method calls on the objects to turn them on, call any number. Print the methods' outcomes;
- turn off both mobiles.

Example output
    `mobile phone 01632-960004 is turned on`

    `mobile phone 01632-960012 is turned on`

    `calling 555-34343`

    `mobile phone is turned off`

    `mobile phone is turned off`
"""


class MobilePhone:
    def __init__(self, number):
        self.number = number

    def turn_on(self):
        return f"mobile phone {self.number} is turned on"

    def turn_off(self):
        return f"mobile phone is turned off"

    def call(self, number):
        return f"calling {number}"


if __name__ == '__main__':
    def main():
        mobile1 = MobilePhone('01632-960004')
        mobile2 = MobilePhone('01632-960012')

        print(mobile1.turn_on())
        print(mobile2.turn_on())
        print(mobile1.call('555-34343'))
        print(mobile1.turn_off())
        print(mobile2.turn_off())


    main()

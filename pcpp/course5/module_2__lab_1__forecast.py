from xml.etree import ElementTree


class TemperatureConverter:
    @staticmethod
    def convert_celsius_to_fahrenheit(deg_celsius: float | int) -> float:
        return (9 / 5) * deg_celsius + 32


class ForecastXMLParser:
    @staticmethod
    def parse() -> None:
        forecast_items = ElementTree.parse('forecast.xml').getroot().iter('item')

        for day, temp_celsius in forecast_items:
            day = day.text
            temp_celsius = float(temp_celsius.text)
            temp_fahrenheit = TemperatureConverter.convert_celsius_to_fahrenheit(temp_celsius)

            print(f"{day}: {temp_celsius:.0f} Celsius, "
                  f"{temp_fahrenheit:.1f} Fahrenheit")


if __name__ == '__main__':
    def main():
        ForecastXMLParser.parse()


    main()


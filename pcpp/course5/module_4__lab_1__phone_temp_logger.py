import logging

FORMAT = "%(levelname)s - %(message)s C"
formatter = logging.Formatter(FORMAT)

handler = logging.FileHandler(filename="battery_temperature.log", mode='w')
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


def log_temperature_if_not_in_accepted_range(temperature_celsius: int):
    if temperature_celsius < 20:
        log = logger.debug
    elif 30 <= temperature_celsius <= 35:
        log = logger.warning
    elif temperature_celsius > 35:
        log = logger.critical
    else:
        return

    log(temperature_celsius)


if __name__ == '__main__':
    import random


    def main():
        temperatures = list(random.choices(range(15, 41), k=10))

        for temp in temperatures:
            log_temperature_if_not_in_accepted_range(temp)


    main()

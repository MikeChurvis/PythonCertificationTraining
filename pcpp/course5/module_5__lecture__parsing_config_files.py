import configparser

config = configparser.ConfigParser()

config_dict = {
    'DEFAULT': {
        'host': 'localhost'
    },
    'mariadb': {
        'name': 'hello',
        'user': 'root',
        'password': 'password'
    },
    'redis': {
        'port': 6379,
        'db': 0
    }
}

config.read_dict(config_dict)
# config.read('config.ini')

print('Sections:', config.sections())
print()

for section in config.sections():
    for config_field in config[section]:
        print(f"{section} :: {config_field} = {config[section][config_field]}")
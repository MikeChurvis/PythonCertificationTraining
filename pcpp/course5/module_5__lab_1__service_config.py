import configparser

config = configparser.ConfigParser()
config.read('mess.ini')

prod_config_dict = {
    section: {
        key: value
        for key, value in config[section].items()
        if key != 'env'
    }
    for section in config.sections()
    if config[section].get('env') == 'prod'
}

dev_config_dict = {
    section: {
        key: value
        for key, value in config[section].items()
        if key != 'env'
    }
    for section in config.sections()
    if config[section].get('env') == 'dev'
}

config = configparser.ConfigParser()
config.read_dict(prod_config_dict)

with open('prod_config.ini', 'w') as prod_config_file:
    config.write(prod_config_file)

config = configparser.ConfigParser()
config.read_dict(dev_config_dict)

with open('dev_config.ini', 'w') as dev_config_dict:
    config.write(dev_config_dict)

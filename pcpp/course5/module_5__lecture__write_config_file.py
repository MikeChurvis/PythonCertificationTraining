import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {'host': 'localhost'}
config['mariadb'] = {'name': 'hello',
                     'user': 'root',
                     'password': 'password'}
config['redis'] = {'port': 6379,
                   'db': 0}

with open('config.ini', 'w') as configfile:
    config.write(configfile)

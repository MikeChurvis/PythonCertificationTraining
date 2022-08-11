import logging

FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

# logging.basicConfig(level=logging.CRITICAL, filename='prod.log', filemode='a', format=FORMAT)

logger = logging.getLogger(__name__)

handler = logging.FileHandler('prod.log', mode='w')
handler.setLevel(logging.CRITICAL)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')

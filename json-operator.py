import json
import yaml
import logging, sys


# Open and handle config.yml
with open('config.yml', 'r') as yml_file:
    config_dict = yaml.safe_load(yml_file)

if config_dict.get('LogLevel').get('level') == 'DEBUG': 
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

input_filename = config_dict.get('Input').get('filename')
key_sorted = config_dict.get('Input').get('sortkey')

logging.debug('filename: ' + input_filename)
logging.debug('sorted based on key: ' + key_sorted)


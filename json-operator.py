import json
import yaml
import logging, sys


# Open the config YAML file
with open('config.yml', 'r') as yml_file:
    config_dict = yaml.safe_load(yml_file)

# Check if we want to be in the debug mode
if config_dict.get('LogLevel').get('level') == 'DEBUG': 
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

input_filename = config_dict.get('Input').get('filename')
key_sorted = config_dict.get('Input').get('sortkey')

logging.debug('filename: ' + input_filename)
logging.debug('sorted based on key: ' + key_sorted)

# Open the JSON file
json_file = open(input_filename)

# Return the JSON object as a dictionary
json_data = json.load(json_file)

# Close the JSON file
json_file.close()
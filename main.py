import yaml
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('commands.yaml') as config_file:
    commands = yaml.safe_load(config_file)

# Getting user input
command = input('> ')

import yaml
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('commands.yaml') as config_file:
    commands = yaml.safe_load(config_file)

def execute(command):
    # Checking the existence of the command
    if command in commands:
        # Checking the type of command
        if commands[command]['type'] == "app":
            apps = commands[command]['path']

            for app in apps:
                os.startfile(app)
            print("Successfully")
    else:
        print("This command doesn't exist")

while True:
    # Getting user input
    command = input('> ')
    execute(command)

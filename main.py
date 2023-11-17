import yaml
import os
import locale
import webbrowser
import sys

with open('config/commands.yaml', 'r', encoding='utf-8') as config_file:
    commands = yaml.safe_load(config_file)

# Set console lang
if locale.getlocale()[0] == "Russian_Russia":
    with open('config/lang/ru_RU.yaml', 'r', encoding='utf-8') as lang_file:
        lang = yaml.safe_load(lang_file)
else:
    with open('config/lang/en_US.yaml', 'r', encoding='utf-8') as lang_file:
        lang = yaml.safe_load(lang_file)


def execute(command: str):
    # Checking the existence of the command
    if command in commands:
        # Checking the type of command

        if commands[command]['type'] == "app":
            apps = commands[command]['path']

            for app in apps:
                os.startfile(app)
            print(lang['command.successfully'])

        elif commands[command]['type'] == "steam":
            id = commands[command]['id']
            webbrowser.open(f'steam://rungameid/{id}')
            print(lang['command.successfully'])


    elif command == 'help':
        for command in commands.keys():
            print(command)
        print('help')
        print('support (contacts)')

    elif command == 'quit' or command == 'exit':
        sys.exit()

    elif command == 'support' or command == 'contacts':
        for line in lang['info.support']:
            print(line)

    else:
        print(lang['command.notfound'])


for line in lang['info.welcome']:
    print(line)

while True:
    # Getting user input
    command = input('> ')
    execute(command)

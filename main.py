import yaml
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Чтение файла конфигурации в формате YAML
with open('commands.yaml') as config_file:
    commands = yaml.safe_load(config_file)

# Получение команды от пользователя
command = input('Введите команду: ')

# Обработка команды
if command in commands:
    # Выполнение команды
    # os.system(commands[command])
    if commands[command]['type']:
        os.startfile(commands[command]['path'])
        print('Команда выполнена')
else:
    print('Команда не найдена')

# Дополнительный код для обработки команд
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
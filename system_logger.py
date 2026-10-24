def log_event(message):
    with open("system.log", "a") as file:
        file.write(message + "\n")
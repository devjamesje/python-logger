# Python Logger by JamesJoynsonEllis

# [Requires datetime]

def logger():
    from datetime import datetime
    file_path = input("File path to log to (.txt is best): ")
    file = open(file_path, "a")
    log = input("LOG: ")
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.today().strftime("%d/%m/%Y")
    log = "<" + current_date + " " + current_time + "> " + log
    file.write("\n")
    file.write(log)

logger()

# This code is not to be directly used without crediting the author

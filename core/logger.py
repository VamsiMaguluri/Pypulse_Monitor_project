import datetime
import os


class DataLogger:
    def __init__(self, folder="logs", filename="system_data.txt"):
        self.path = os.path.join(folder, filename)
        # Create the logs folder if it doesn't exist
        if not os.path.exists(folder):
            os.makedirs(folder)

    def log_data(self, cpu_info, mem_info):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} | {cpu_info} | {mem_info}\n"

        with open(self.path, "a") as file:
            file.write(log_entry)
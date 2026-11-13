from datetime import datetime
import os

def log_event(message):

    os.makedirs("logs", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("logs/attacks.log", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")
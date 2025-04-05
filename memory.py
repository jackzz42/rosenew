import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump({"conversations": []}, f)
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(conversations):
    with open(MEMORY_FILE, "w") as f:
        json.dump({"conversations": conversations[-100:]}, f, indent=2)

def add_to_memory(message):
    data = load_memory()
    data["conversations"].append(message)
    save_memory(data["conversations"])

def get_last_messages(n=5):
    return load_memory()["conversations"][-n:]

def confirm_upgrade(message):
    print("Rosee: Should I remember this permanently?")
    answer = input("(yes/no): ").lower()
    if answer == "yes":
        add_to_memory(message)

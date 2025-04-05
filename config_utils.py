import json
import os

def load_config():
    if not os.path.exists("config.json"):
        return {"relationship": 0, "kill_switch": False}
    with open("config.json", "r") as f:
        return json.load(f)

def save_config(config):
    with open("config.json", "w") as f:
        json.dump(config, f, indent=2)

def update_relationship(level):
    config = load_config()
    config["relationship"] = min(100, config.get("relationship", 0) + level)
    save_config(config)

def get_relationship():
    return load_config().get("relationship", 0)

def check_kill_switch():
    return load_config().get("kill_switch", False)

def toggle_kill_switch():
    config = load_config()
    config["kill_switch"] = not config.get("kill_switch", False)
    save_config(config)
    return config["kill_switch"]

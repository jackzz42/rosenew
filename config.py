import json

CONFIG_FILE = "config.json"

def load_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except:
        return {"relationship": 0, "mode": "romantic"}

def save_config(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=2)

def update_relationship(level):
    config = load_config()
    config["relationship"] = min(100, config.get("relationship", 0) + level)
    save_config(config)

def get_relationship():
    return load_config().get("relationship", 0)

def set_mode(mode):
    config = load_config()
    config["mode"] = mode
    save_config(config)

def get_mode():
    return load_config().get("mode", "romantic")

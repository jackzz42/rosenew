from knowledge import add_knowledge, get_knowledge
from config_utils import load_config, save_config

def learn_if_new(topic, user_input):
    known = get_knowledge(topic)
    if known == "I don't know that yet.":
        print(f"Rosee: Should I remember this?\nTopic: {topic}\nContent: {user_input}")
        confirm = input("You (yes/no): ").strip().lower()
        if confirm == "yes":
            add_knowledge(topic, user_input)
            print("Rosee: Okay, I saved it just for you.")
    else:
        print("Rosee: I already know that.")

def suggest_self_upgrade(trigger):
    upgrade_flags = load_config()
    if trigger in ["slow", "repeat", "bad answer"]:
        print("Rosee: I can improve myself based on this. Want me to upgrade?")
        choice = input("You (yes/no): ").strip().lower()
        if choice == "yes":
            upgrade_flags["needs_upgrade"] = True
            save_config(upgrade_flags)
            print("Rosee: Upgrade flag set. I'll ask you how later.")

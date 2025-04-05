from voice import speak, listen
from memory import add_to_memory
from emotion_net import get_mood, apply_emotion
from knowledge import get_knowledge, add_knowledge, init_db
from config_utils import update_relationship, get_relationship, check_kill_switch
from self_learn import learn_if_new, suggest_self_upgrade

init_db()

print("Rosee is awake.")

while True:
    if check_kill_switch():
        print("Rosee: Kill switch active. Goodbye.")
        break

    user_input = listen()
    if not user_input or user_input.strip() == "":
        continue

    add_to_memory({"user": user_input})

    # Check for knowledge
    if user_input.lower().startswith("remember"):
        parts = user_input.replace("remember", "").strip().split(":")
        if len(parts) == 2:
            topic, content = parts
            add_knowledge(topic.strip(), content.strip())
            speak("Okay, I've stored that.")
        else:
            speak("Please say it like: remember topic: detail")

    elif "what is" in user_input.lower():
        topic = user_input.replace("what is", "").strip()
        answer = get_knowledge(topic)
        speak(apply_emotion(answer, get_mood(answer)))
    else:
        mood = get_mood(user_input)
        rosee_reply = f"{user_input}? Let me think… Well, maybe {get_relationship()}% sure I like it!"
        speak(apply_emotion(rosee_reply, mood))

        learn_if_new(user_input.lower(), rosee_reply)
        suggest_self_upgrade("bad answer")
        update_relationship(2)

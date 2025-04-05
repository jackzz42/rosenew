from voice import listen, speak_emotionally
from memory import add_to_memory, get_last_messages, confirm_upgrade
from knowledge import add_knowledge, get_knowledge, init_db
from config import update_relationship, get_relationship, set_mode, get_mode
from emotion_net import predict_emotion

init_db()

print("Rosee: Ready to talk. Say 'emergency mode' to enter work-only mode.")

while True:
    user_input = listen().lower()

    if "shutdown" in user_input or "kill switch" in user_input:
        print("Rosee shutting down.")
        break

    if "emergency mode" in user_input:
        set_mode("work")
        speak_emotionally("Emergency mode activated. I will only assist you.")
        continue
    elif "back to normal" in user_input:
        set_mode("romantic")
        speak_emotionally("Back to normal now!")
        continue

    if "remember" in user_input:
        confirm_upgrade(user_input)
        speak_emotionally("Okay, saved this in memory.")
        continue

    if "what is" in user_input:
        topic = user_input.replace("what is", "").strip()
        answer = get_knowledge(topic)
        if answer:
            speak_emotionally(answer)
        else:
            speak_emotionally("I don't know yet.")
        continue

    mood = predict_emotion(user_input)
    speak_emotionally(f"{user_input}")
    update_relationship(1)

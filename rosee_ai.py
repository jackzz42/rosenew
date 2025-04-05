import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from voice import speak, listen
from emotion_net import predict_emotion
from memory import add_to_memory, get_last_messages
from knowledge import add_knowledge, get_knowledge, init_db
from relationship import update_relationship, get_relationship
from utils import detect_emergency, kill_switch_triggered

torch.set_default_dtype(torch.float32)
init_db()

model_path = "C:/Users/Acer/Downloads/roseeai/deepseek-7b"

tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    local_files_only=True,
    torch_dtype=torch.float32
)

def think_and_reply(prompt):
    memory = get_last_messages()
    history = "\n".join([f"You: {m['user']}\nRosee: {m['rosee']}" for m in memory])
    full_prompt = f"{history}\nYou: {prompt}\nRosee:"

    inputs = tokenizer.encode(full_prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_new_tokens=200, do_sample=True, temperature=0.7)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).split("Rosee:")[-1].strip()
    return response

def chat():
    while True:
        if kill_switch_triggered():
            print("Kill switch activated. Rosee is off.")
            break

        user_input = listen()
        if not user_input:
            continue

        if detect_emergency(user_input):
            speak("Okay. Switching to emergency assistant mode.")
            continue

        emotion = predict_emotion(user_input)
        response = think_and_reply(user_input)
        memory_entry = {"user": user_input, "rosee": response}
        add_to_memory(memory_entry)

        if "remember" in user_input.lower():
            topic = user_input.split("remember")[-1].strip()
            add_knowledge(topic, response)
            speak("Got it. I’ll remember that.")
        elif "what is" in user_input.lower():
            topic = user_input.lower().split("what is")[-1].strip().rstrip("?")
            answer = get_knowledge(topic)
            speak(answer)
        else:
            final_response = apply_emotion_voice(response, emotion)
            speak(final_response)

if __name__ == "__main__":
    chat()

import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import AutoTokenizer

class EmotionRNN(nn.Module):
    def __init__(self, vocab_size, hidden_dim, output_size):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, 128)
        self.lstm = nn.LSTM(128, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_size)

    def forward(self, x):
        embedded = self.embedding(x)
        lstm_out, _ = self.lstm(embedded)
        last_output = lstm_out[:, -1, :]
        return self.fc(last_output)

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = EmotionRNN(vocab_size=tokenizer.vocab_size, hidden_dim=64, output_size=4)
model.load_state_dict(torch.load("emotion_model.pth", map_location=torch.device("cpu")))
model.eval()

labels = ["friendly", "romantic", "angry", "caring"]

def predict_emotion(text):
    tokens = tokenizer.encode(text, return_tensors="pt", truncation=True, max_length=30)
    with torch.no_grad():
        output = model(tokens)
        pred = torch.argmax(F.softmax(output, dim=1))
    return labels[pred]

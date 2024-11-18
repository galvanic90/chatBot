import nltk

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

# nltk.download('punkt_tab')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

chatbot = ChatBot("Sebatian")

trainer = ListTrainer(chatbot)

# Leer el archivo de entrenamiento
with open("train_data_copilot.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Procesar los datos del archivo
training_data = []
for line in lines:
    question, answer = line.strip().split('","')
    question = question.strip('"')
    answer = answer.strip('"')
    training_data.append([question, answer])

for pair in training_data:
    trainer.train(pair)

exit_conditions = (":q", "quit", "exit")

while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        response = chatbot.get_response(query)
        if float(response.confidence) < 0.5:  # Ajusta el umbral de confianza según sea necesario
            print("🤖Lo siento, solo sé cosas sobre GitHub Copilot.")
        else:
            print(f"🤖 {response}")
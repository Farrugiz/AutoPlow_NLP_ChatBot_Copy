from neuralintents import GenericAssistant

assistant = GenericAssistant("C:\\Users\\Zacha\\Python\\chat\\intents_test.json", model_name="test_model")
assistant.train_model()
assistant.save_model()

done = False

while not done:
    text = input("Enter a text: ")
    text = text.lower()
    if text == "stop":
        done = True
    else:
        assistant.request(text)
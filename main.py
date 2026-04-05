from router import classify_intent
import json

print("Intent Router Started (type 'exit' to stop)\n")

while True:
    user_input = input("Enter input: ")

    if user_input.lower() == "exit":
        break

    result = classify_intent(user_input)
    print(json.dumps(result, indent=4))
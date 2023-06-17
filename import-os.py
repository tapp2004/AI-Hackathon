import os
import openai

openai.organization = "org-5DYcOkPe34yzGHX58UjKe53Y"
openai.api_key = "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"
openai.Model.list()

openai.Model.retrieve("text-davinci-003")

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)

saved_message = completion.choices[0].message

{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello!"}]
}

{
    "id": "chatcmpl-123",
    "object": "chat.completion",
    "created": 1677652288,
    "choices": [{
        "index": 0,
        "message": {
            "role": "assistant",
            "content": "\n\nHello there, how may I assist you today?",
        },
        "finish_reason": "stop"
    }],
    "usage": {
        "prompt_tokens": 9,
        "completion_tokens": 12,
        "total_tokens": 21
    }
}

print("Welcome to the Vacation Chatbot!")
print("Enter your prompts or descriptions of your ideal vacation below. Type 'exit' to quit.")

while True:
    user_input = input("> ")

    if user_input.lower() == "exit":
        break

    response = openai.Completion.create(
        engine="text-davinci-003",  # Specify the language model you want to use
        prompt=user_input,
        max_tokens=100  # Set the maximum length of the generated response
    )

    generated_text = response.choices[0].text.strip()
    print("Chatbot: " + generated_text)

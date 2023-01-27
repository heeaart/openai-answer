import openai

# Ustawienie klucza API
openai.api_key = "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"

# Twoje pytanie
print("Zadaj mi pytanie ")
pytanie = input()

# Zadanie pytania openai
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"{pytanie}",
    max_tokens=1024
)

# Wyświetlenie odpowiedzi
print(response["choices"][0]["text"])



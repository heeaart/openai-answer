import openai

# Ustawienie klucza API https://beta.openai.com/account/api-keys
openai.api_key = "twoj-klucz-api"

# Twoje pytanie
print("Zadaj mi pytanie ")
pytanie = input()

# Wysłanie requesta
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"{pytanie}",
    max_tokens=1024
)

# Wyświetlenie odpowiedzi
print(response["choices"][0]["text"])



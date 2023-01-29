import os
import openai

from colorama import init as colorama_init
from colorama import Fore
from dotenv import load_dotenv

load_dotenv()

colorama_init()

# Ustawienie klucza API https://beta.openai.com/account/api-keys
openai.api_key = (os.getenv('TOKEN-API'))

# Twoje zapytanie
def odp(wiadomosc):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=wiadomosc,
        temperature=0.5,
        max_tokens=1024
    )

    return response['choices'][0]['text']

# Rozmowa z openai
while True:
    wiadomosc = input(f"{Fore.WHITE}👨‍💻 Ty: ")
    if wiadomosc == "Narka":
        print(f"{Fore.RED}👋 Elo do zobaczenia")
        break
    else:
        print(f"{Fore.BLUE}🤖 Bot: {odp(wiadomosc)} {Fore.BLACK} \n{Fore.YELLOW}⚠️ Aby zakończyć napisz `Narka`")


import requests
from time import sleep
from dotenv import load_dotenv
import os


def api(TOKEN, BASE_URL):
    r = requests.get(BASE_URL + "getMe")

    if r.status_code != 200:
        print("Bot offline encerrando processo")
        return

    print("Bot online, OK")
    offset = None
    while True:
        polingUpdate = getUpdates(TOKEN,BASE_URL, offset=offset)

        if polingUpdate is not None:
            
            offset = int(polingUpdate["update_id"]) + 1

            recivedMessage(BASE_URL,polingUpdate["message"])
        


#message sera um objeto complexo contendo todos os dados da mensagem
def recivedMessage(BASE_URL,message = None):  # noqa: F811
    if message is None:
        return None
    
    chat_id = message["chat"]["id"]
    user_first_name = message["chat"]["first_name"]


    params = {"chat_id": chat_id,"text":f"hello {user_first_name}"}

    requests.post(BASE_URL+"sendMessage",params=params)
    


def getUpdates(TOKEN, BASE_URL, offset=None):
    # OffSet Definindo apartir de qual mensagem pegar sendo a primeira a mais importante

    params = {"timeout": 5, "offset": offset}
    r = requests.get(BASE_URL + "getUpdates", params=params)

    print(r.json())

    if "result" not in r.json():
        return None

    if len(r.json()["result"]) <= 0:
        return None
    
    # Para pegar as proximas mensagens
    return r.json()["result"][0]


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"
api(TOKEN=TOKEN, BASE_URL=BASE_URL)

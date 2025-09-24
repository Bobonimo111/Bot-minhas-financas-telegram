import requests
from time import sleep
from dotenv import load_dotenv
import os




 
def api(TOKEN, BASE_URL):
    r = requests.get(BASE_URL+"getMe")

    if(r.status_code != 200):
        print("Bot offline encerrando processo")
        return
    
    print("Bot online, OK")
    offset = None
    while(True):
        
        # OffSet Definindo apartir de qual mensagem pegar sendo a primeira a mais importante
        params = {"timeout": 10,"offset":offset}
        r = requests.get(BASE_URL+"getUpdates",params=params)

        polingUpdate = bot(r,offset=offset)
        
        if(polingUpdate != None):
            print(polingUpdate["message"]["text"])
            offset = int(polingUpdate["update_id"]) + 1
        
        
def bot(r,offset = None):
    print(r.json())

    if(("result" not in r.json())):
        return None
    
    if(len(r.json()["result"]) <= 0):
        return None
   # Para pegar as proximas mensagens
    return r.json()["result"][0]
 
 
load_dotenv()
 
TOKEN =  os.getenv("BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"
api(TOKEN=TOKEN,BASE_URL=BASE_URL)
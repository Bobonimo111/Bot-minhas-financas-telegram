from curses import keyname
import requests
from time import sleep
from dotenv import load_dotenv
import os


def api(TOKEN, BASE_URL,timeout):
    r = requests.get(BASE_URL + "getMe")

    if r.status_code != 200:
        print("Bot offline encerrando processo")
        return

    print("Bot online, OK")
    offset = None
    while True:
        polingUpdate = getUpdates(BASE_URL, offset=offset,timeout=timeout)
        print(polingUpdate)
        if (polingUpdate is not None) :
            print("Updater não esta vazio")
            offset = int(polingUpdate["update_id"]) + 1
            #My_chat_member serve para outra coisa no chat 
            #new_chat_member São configurações de grupo 
            if "my_chat_member" not in polingUpdate and "new_chat_member" not in polingUpdate["message"]: 
                #Aq contemos dados como id,first_name,type
                messageObj =  polingUpdate["message"]
                chatObj = {
                    "id": messageObj["chat"]["id"],
                    "title": messageObj["chat"]["title"] if "title" in messageObj["chat"] else None,
                    "type":  messageObj["chat"]["type"]
                }
                
                #Aq temos o texto enviado no chat ou ate para o proprio bot
                textData = {
                    "text":messageObj["text"], 
                    "date":messageObj["date"],
                    "first_name":messageObj["from"]["first_name"]
                }
                
                if chatObj["type"] != "private":
                    confirmMessage = commandsController(textData=textData);
                    sendMessage(BASE_URL,confirmMessage,chat_id=chatObj["id"])
        


#message sera um objeto complexo contendo todos os dados da mensagem
def sendMessage(BASE_URL,text,chat_id = None):  # noqa: F811
    if chat_id is None or text is None:
        print(f"Valores chat_id:{chat_id} ou text:{text} None mensagem não enviada")
        return None

    print(f"Enviado messagem: {text} para o chatId : {chat_id}")
    params = {"chat_id": chat_id,"text":text}

    requests.post(BASE_URL+"sendMessage",params=params)


def getUpdates(BASE_URL, offset=None,timeout = 5):
    # OffSet Definindo apartir de qual mensagem pegar sendo a primeira a mais importante
    params = {"timeout": timeout, "offset": offset}
    r = requests.get(BASE_URL + "getUpdates", params=params)

    # print(r.json())

    if "result" not in r.json():
        return None

    if len(r.json()["result"]) <= 0:
        return None
    
    # Para pegar as proximas mensagens
    return r.json()["result"][0]


def commandsController(textData):
    print("Cotroller commands iniciado")
    
    
    #Processa a mensagem para retirar o comando e armazenar a mensagem
    breakText = (textData["text"].strip()).split(" ")
    command = breakText[0]
    text = " ".join(breakText[1:])
        
    #Essa função de controle, aonde os comandos vão ser tratados e executados
    commands = {
    "/start": {
        "desc": "Inicia o bot e mostra mensagem de boas-vindas",
        "func": lambda: welcomeMessage(textData["first_name"]),  # type: ignore
    },
    "/save": {
        "desc": "Salvar compra no banco de dados",
        "func": lambda: saveInDataBase(text),
    },
    "/list": {
        "desc": "Listar todas as compras sem data",
        "func": lambda: listAllShoppingWithOutDate(),
    },
    "/ldat": {
        "desc": "Listar todas as compras entre datas",
        "func": lambda: listAllShoppingBetweenDates(),
    },
    "/expe": {
        "desc": "Total de despesas sem data",
        "func": lambda: getTotalExpensesgWithOutDate(),
    },
    "/edat": {
        "desc": "Total de despesas entre datas",
        "func": lambda: getTotalExpensesBetweenDate(),
    },
    "/cat": {
        "desc": "Criar nova categoria no banco de dados",
        "func": lambda: createNewCategoryInDataBase(),
    },
    }

    
    #Confirma sé um comando ou não
    if("/" not in textData["text"][0]):
        msg = "Comandos disponiveis: "
        for c in commands.keys():
            msg += f"\n {c}"
        return msg
  
    if command not in commands:
        msg = "Comando não encontrado: "
        for c in commands.keys():
            msg += f"\n {c}"
        return msg
    
    print("Cotroller retornando valor")
    funcInstance = commands.get(f"{command}").get("func")
    mensageReturn = funcInstance()
    print(f"Mensagem de retorno: {mensageReturn}")
    return mensageReturn

    
def welcomeMessage(userName = None):
    print("função welcomeMessage iniciada!")
    return f"Grettings Welcome! {userName}"

def saveInDataBase(text):
    return "Not Implemented"
    
def listAllShoppingWithOutDate():
    return "Not Implemented"
    
def listAllShoppingBetweenDates():
    return "Not Implemented"

def getTotalExpensesgWithOutDate():
    return "Not Implemented"
    
def getTotalExpensesBetweenDate():
    return "Not Implemented"    
    
def createNewCategoryInDataBase():
    return "Not Implemented"
    
    
#================================================================
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"
api(TOKEN=TOKEN, BASE_URL=BASE_URL,timeout=5)

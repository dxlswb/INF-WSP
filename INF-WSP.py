import requests
import os
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
os.system("clear")

print(BLUE+"█ █▄░█ █▀▀ ▄▄ █░█░█ █▀ █▀█")
pronto("    █ █░▀█ █▀░ ░░ ▀▄▀▄▀ ▄█ █▀▀")

print("\033[33m--------------------------------------")
print(RED+"Autor:dxlswb")
print("--------------------------------------")
print(WHITE+"TIK TOK: dxlswb")
print("--------------------------------------")
print(WHITE+"escribe el numero de el whatsapp junto\ncon el prefijo, ejemplo: +526621745707\n")

api_key = '7e1cadf1fc1587fd37db7ea1e6c29a50'

number = int(input(GREEN+"Numero de telefono: "+RESET))

data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, numb>

for key, value in data.json().items():

    print("%s: %s" % (key, value))

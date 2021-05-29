import platform, sys, os, platform, time, whois
from Dark import Opcoes
Opcoes = Opcoes()
logo = """______           _                  
|  _  \         | |                 
| | | |__ _ _ __| | __              
| | | / _` | '__| |/ /              
| |/ / (_| | |  |   <               
|___/ \__,_|_|  |_|\_\              
                                       
           (_)                      
 _ __  _ __ ___   ____ _  ___ _   _ 
| '_ \| '__| \ \ / / _` |/ __| | | |
| |_) | |  | |\ V / (_| | (__| |_| |
| .__/|_|  |_| \_/ \__,_|\___|\__, |
| |                            __/ |
|_|                           |___/ 
 _                                  
| |                                 
| |_ ___  __ _ _ __ ___             
| __/ _ \/ _` | '_ ` _ \            
| ||  __/ (_| | | | | | |           
 \__\___|\__,_|_| |_| |_|

 """

opcoes = {"0": "ATTACK DoS",#ok
          "1": "Pegar Cdg. Fonte da pag",#ok
          "2": "Url Scan",#ok
          "3": "sqlmap e instruções em português",#ok
          "4": "Bomb De SMS", #oky
          "5": "Instalar Todas Dependencias",#okay
          "6": "Team de conhecimento",
          "7": "Port Scan",#ok
          "8": "Video e Imagem, Downloader",#ok
          "99": "Sair"}

def Inicio():
  if platform.system() == "Windows": os.system('cls')
  else: os.system('clear')
  print(logo)
  print(f"$ -- SO - {platform.system()} --$\n")
  for i in opcoes:
    print(f'-> [{i}] - [{opcoes[i]}]')
  while True:
    escolha = int(input("$ "))
    if(escolha == 0):
      Opcoes.Dos()
      Inicio()
    if(escolha == 1):
      Opcoes.PegarCodigoFonte()
      Inicio()
    if(escolha == 2):
      Opcoes.SiteScan()
      Inicio()
    if(escolha == 3):
      Opcoes.SqlMap()
      Inicio()
    if(escolha == 4):
      Opcoes.BombTroll()
      Inicio()
    if(escolha == 5):
      Opcoes.InstalarPacotes()
      Inicio()
    if(escolha == 6):
      Opcoes.Team()
      Inicio()
    if(escolha == 7):
      Opcoes.PortScan()
      Inicio()
    if(escolha == 8):
      Opcoes.Download()
      Inicio()
    if(escolha == 99):
      sys.exit()

Inicio()

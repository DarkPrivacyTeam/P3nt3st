import time
import os
import platform
import requests
import socket
import whois
import Utils as ultilidades

class Opcoes(object):
	def BombTroll(self):
		print ("VOCE TEM 10 SEGUNDOS PRA REINICIA O SEU APARELHO E IMPEDIR QUE ELE SEJA FORMATADO.")

		for a in range(1, 10):
			time.sleep(1)
			print("\n{}".format(a))
		print ("\n\nRELAXA CORAI E ZUERA KKKKKK")

	def Dos(self):
		if platform.system() == "Windows": os.system('cls');
		else: os.system('clear')
		a = """ ██████████             █████████ 
	░░███░░░░███           ███░░░░░███
	 ░███   ░░███  ██████ ░███    ░░░ 
	 ░███    ░███ ███░░███░░█████████ 
	 ░███    ░███░███ ░███ ░░░░░░░░███
	 ░███    ███ ░███ ░███ ███    ░███
	 ██████████  ░░██████ ░░█████████ 
	░░░░░░░░░░    ░░░░░░   ░░░░░░░░░  
									  
									  
									  """
		print (a)
		print ("\n\nINICIALIZANDO....")
		time.sleep(1)
		input("\nSE VOCE N INSTALOR OS PACOSTES PRICIPAIS ABRA UMA NOVA SESSAO\nE ABRA A FERRREMENTA E INSTALLE, \nMAIS SE JA TIVER INSTALADO APERTER\nENTER....   ")
		try:
			print ("INDO PRA A FERRAMENTA DE DoS FEITA\nPOR SASAKI DA BLACK HELL TEAM...")
			time.sleep(2)
			os.system('git clone https://github.com/Black-Hell-Team/Power-DoS')
			os.system('cd Power-DoS; chmod +x *; python3 powerdos.py')
		except:
			print ("\n\nNAO FOI POSSIVEL INICIALIZAR A FERRAMENTA POR FAVOR REINICIE O SCRIPT.")

	def Download(self):
		url = input("Digite a Url: ")
		nome = input("Nome do arquivo a ser salvo, com extensão: ")
		linkValido = ultilidades.ValidarLink(url)
		if linkValido == 1:
			container = requests.get(url)
			try:
				with open(f'{nome}', 'wb') as arquivo:
					arquivo.write(container.content)
				print("Arquivo salvo")
			except Exception as erro:
				print(f"Erro ao salvar arquivo - {str(erro)}")

	def PegarCodigoFonte(self):
		logo = """
		██████  ███████  ██████  █████     ██████  ██████  ██████ 
		██   ██ ██      ██       ██   ██   ██      ██  ██  ██   ██
		██████  █████   ██  ███  ███████   ██      ██  ██  ██   ██
		██      ██      ██   ██  ██   ██   ██      ██  ██  ██   ██
		██      ███████  ██████  ██   ██   ██████  ██████  ██████

																	  
		███████  ██████  ███    ██ ████████ ███████                  
		██       ██  ██  ████   ██    ██    ██                  
		█████    ██  ██  ██ ██  ██    ██    █████                    
		██       ██  ██  ██  ██ ██    ██    ██                   
		██       ██████  ██   ████    ██    ███████

		By: System - Mickey</>
		""" 
		ultilidades.Limpar()
		print(logo)

		url = input("Url $ ")

		codigo_fonte = requests.get(url)
		if codigo_fonte.status_code == 200: 
			print(codigo_fonte.text); time.sleep(2) 
			try:
				ultilidades.Limpar()
				ultilidades.SalvaArquivo(codigo_fonte.text)
				print("Arquivo com informações salvas!")
			except Exception as erro: 
				print("Erro ao salvar informações", str(erro))
		else: print("Não foi possivel dar get nessa url!")

		input("Pressione Enter para sair....")
		ultilidades.Limpar()

	def InstalarPacotes(self):
		os.system('apt update; apt upgrade; pkg install nmap; pkg install python; pkg install tsu; pkg install wget; ')

	def PortScan(self):
		print ("VERIFICA AS PORTAS QUE ESTAO ABERTA [1]\nVERIFICA AS PORTAS MAIS IMPORTATES [2]")

		opcao= int(input("\n\n---$"))

		if opcao == 1:
			ip = input("\nDIGITE SEU IP -$ ")

			for porta in range(1, 65535):
				_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				if _socket.connect_ex((ip, porta)) == 0:
					print ("\nPorta", porta ,"[ABERTA] - SEU [IP]: {}".format(ip))
					_socket.close()

		elif opcao == 2:
			ip = input("\nDiGITE SEU IP -$ ")
			portas = [21, 23, 80, 443, 8080, 88]
			for porta in portas:
				 _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				 _socket.settimeout(0.1)
				 respota = _socket.connect_ex((ip, porta))
				 if respota  == 0: print(porta, "OPEN")
				 elif respota != 0: print(porta, "CLOSED")
		time.sleep(20)
	def SiteScan():
		os.system('pip install python-whois')
		ultilidades.Limpar()
		site = input("site~# ")
		who1 = whois.whois(site)
		print(who1.text)
		time.sleep(80)

	def SqlMap(self):
		print ("[1] -> INSTRUÇOES EM PORTUGUES\n[2] -> SQLMAP")

		sql = int(input("\n---$ "))

		if sql == 1:
			print("""Opções:
		  -h, --help Mostra a mensagem de ajuda básica e sai
		  -hh Mostra a mensagem de ajuda avançada e sai
		  --version Mostra o número da versão do programa e sai
		  -v VERBOSE Nível de verbosidade: 0-6 (padrão 1)

		  Alvo:
			Pelo menos uma dessas opções deve ser fornecida para definir o
			alvo (s)

			-u URL, --url = URL URL de destino (por exemplo, "http://www.site.com/vuln.php?id=1")
			-g GOOGLEDORK Processa os resultados do Google Dork como URLs de destino

		  Solicitação:
			Essas opções podem ser usadas para especificar como se conectar ao URL de destino

			--data = DATA String de dados a ser enviada por meio de POST (por exemplo, "id = 1")
			--cookie = valor do cabeçalho do cookie HTTP COOKIE (por exemplo, "PHPSESSID = a8d127e ..")
			--random-agent Usa o valor do cabeçalho do Agente do Usuário HTTP selecionado aleatoriamente
			--proxy = PROXY Use um proxy para se conectar ao URL de destino
			--tor Use a rede de anonimato Tor
			--check-tor Verifique se o Tor está sendo usado corretamente

		  Injeção:
			Essas opções podem ser usadas para especificar quais parâmetros testar,
			fornecer cargas úteis de injeção personalizadas e scripts opcionais de adulteração

			-p TESTPARAMETER Parâmetro (s) testável (s)
			--dbms = DBMS Força o DBMS de back-end a fornecer o valor

		  Detecção:
			Essas opções podem ser usadas para personalizar a fase de detecção

			--level = LEVEL Nível de testes a serem executados (1-5, padrão 1)
			--risk = RISK Risco de testes a serem realizados (1-3, padrão 1)

		  Técnicas:
			Essas opções podem ser usadas para ajustar o teste de injeção SQL específica
			técnicas

			--technique = TECH .. Técnicas de injeção de SQL para usar (padrão "BEUSTQ")

		  Enumeração:
			Essas opções podem ser usadas para enumerar o banco de dados back-end
			informações do sistema de gestão, estrutura e dados contidos no
			mesas

			-a, --all Recupera tudo
			-b, --banner Recuperar banner DBMS
			--current-user Recupera o usuário atual do DBMS
			--current-db Recupera banco de dados atual do DBMS
			--passwords Enumera hashes de senha de usuários DBMS
			--tables Enumerar tabelas de banco de dados DBMS
			--columns Enumerar colunas da tabela de banco de dados DBMS
			--schema Enumerar esquema DBMS
			--dump Dump entradas da tabela de banco de dados DBMS
			--dump-all Dump
			
			Despejar todas as entradas de tabelas de bancos de dados DBMS
			-D banco de dados DB DBMS para enumerar
			-T Tabela (s) de banco de dados TBL DBMS para enumerar
			-C COL DBMS coluna (s) da tabela de banco de dados para enumerar

		  Acesso ao sistema operacional:
			Essas opções podem ser usadas para acessar o gerenciamento de banco de dados de back-end
			sistema sistema operacional subjacente

			--os-shell Prompt para um shell de sistema operacional interativo
			--os-pwn Prompt para um shell OOB, Meterpreter ou VNC

		  Em geral:
			Estas opções podem ser usadas para definir alguns parâmetros gerais de trabalho

			--batch Nunca peça a entrada do usuário, use o comportamento padrão
			--flush-session Esvaziar arquivos de sessão para o destino atual

		  Diversos:
			Essas opções não se enquadram em nenhuma outra categoria

			--wizard Interface de assistente simples para usuários iniciantes
			  """)
			time.sleep(10)

		if sql == 2:
			os.system('git clone https://github.com/sqlmapproject/sqlmap')
			os.system('cd sqlmap; chmod +x *; python2 sqlmap.py')

	def Team(self):
		print ('gerando link...')
		time.sleep(1)
		print('\nlink da team: https://chat.whatsapp.com/E9JEBGe8MxL0BBB5GUnWXM')
		time.sleep(10)

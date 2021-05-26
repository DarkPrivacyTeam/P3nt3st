import os, platform, requests

def Limpar():
	if platform.system() == "Windows": os.system('cls');
	else: os.system('clear')

def SalvaArquivo(texto):
	with open(f'codigoFonte.txt', 'w') as arquivo:
		arquivo.write(texto)

def ValidarLink(url):
	try:
		resposta = requests.get(url)
		if resposta.status_code == 200:
			print(f"Link valido! - {resposta}")
			return 1
		else:
			print(f"Link invalido! - {resposta}")
			return 0
	except Exception as erro:
		print(f"Houve um erro na sua url - {str(erro)}")
		return 0

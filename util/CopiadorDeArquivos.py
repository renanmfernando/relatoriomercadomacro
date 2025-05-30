import os, shutil, sys

def copia(pastaFonte, pastaDestino):

	for arquivo in os.listdir(pastaFonte):
		caminhoDe = os.path.join(pastaFonte, arquivo)
		try:
			if os.path.isfile(caminhoDe):
				caminhoPara = os.path.join(pastaDestino, arquivo)
				shutil.copyfile(caminhoDe, caminhoPara)
		except Exception as e:
			print('Não foi possível copiar arquivo: ' + e)
import os
import time
from .CopiadorDeArquivos import copia

def fazDeploy():

	fazDeployEmPasta('C:\\Tadeu\\Fontes\\C#\\LagunaProducao\\Trunk\\Laguna.WindowsForms\\bin\\Release', 'F:\\HOME\\CONTROLE\\Laguna\\provisorio')	
	time.sleep(10)
	fazDeployEmPasta('C:\\Tadeu\\Fontes\\C#\\LagunaProducao\\Trunk\\Laguna.WindowsForms\\bin\\Release', 'F:\\HOME\\BCO\\APL64\\Mvc\\Laguna')
	
def fazDeployEmPasta(pastaOrigem, pastaDestino):
	pastaProducao = pastaDestino
	for arquivo in os.listdir(pastaProducao):
		caminho = os.path.join(pastaProducao, arquivo)
		try:
			if os.path.isfile(caminho):
				os.unlink(caminho)
		except Exception as e:
			print(e)

	pastaRelease = pastaOrigem
			
	copia(pastaRelease, pastaProducao)
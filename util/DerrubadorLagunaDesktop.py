from .deployLaguna import fazDeploy
import time
from util.LagunaAPI import postAPI

def derruba():

	print('Derrubar em 6h')
	time.sleep(60 * 60 * 6)
	resposta = postAPI('RotinaFimDoDia', 'derrubaLaguna')
	print(resposta)
	print('Esperando derrubar')
	time.sleep(40)
	print('Realizando deploy')
	fazDeploy()
	print('Fez deploy')
	return resposta
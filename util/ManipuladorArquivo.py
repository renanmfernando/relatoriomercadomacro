import os, shutil, sys, glob, zipfile
from pathlib import Path

_textoSubstring = "123"

def getPastaDownloads():
   return os.path.expanduser("~\\downloads")

def geraArquivo(nomeArquivo, conteudo: str): 
    arquivo = open(nomeArquivo, 'w')
    arquivo.write(conteudo)
    arquivo.close()

def geraArquivoDeLinhas(nomeArquivo, linhas): 
    arquivo = open(nomeArquivo, 'w')

    for linha in linhas:
        arquivo.write(linha)
    
    arquivo.close()

def copia(pastaFonte, pastaDestino):

	for arquivo in os.listdir(pastaFonte):
		caminhoDe = os.path.join(pastaFonte, arquivo)
		try:
			if os.path.isfile(caminhoDe):
				caminhoPara = os.path.join(pastaDestino, arquivo)
				shutil.copyfile(caminhoDe, caminhoPara)
		except Exception as e:
			print('Não foi possível copiar arquivo: ' + e)


def copiaArquivo(caminhoArquivo, pastaDestino):

	try:
		if os.path.isfile(caminhoArquivo):
			shutil.copyfile(caminhoArquivo, pastaDestino)
			print('Arquivo ' + caminhoArquivo + ' copiado para ' + pastaDestino)
	except Exception as e:
		print('Não foi possível copiar arquivo: ' + e.__str__())

def getCaminhoArquivoMaisRecente(pasta: str, prefixoNomeArquivo: str) -> str:

    if  os.path.exists(pasta) == False:
        os.makedirs(pasta)

    arquivosDePasta = glob.glob(pasta + "\\*")
    _textoSubstring = prefixoNomeArquivo

    bla = filter(lambda x : x.find(prefixoNomeArquivo) != -1 , arquivosDePasta)

    arquivosDePasta = list(bla)

    arquivoAcopiar = max(arquivosDePasta, key=os.path.getctime)

    return arquivoAcopiar

def contemZip(minhaString: str) -> bool:
   if(minhaString.find(".zip") != -1):
      return True
   else:
      return False

def unzipaArquivos(caminhoPasta: str):

    arquivosDePasta = glob.glob(caminhoPasta + "\\*")
    _textoSubstring = ".zip"

    arquivosDePasta = filter(contemZip, arquivosDePasta)

    caminhoArquivoZip = max(arquivosDePasta, key=os.path.getctime)
    z = zipfile.ZipFile(caminhoArquivoZip, 'r')
    
    z.extractall(caminhoPasta)

def getArquivosDePastaQueContemString(pasta: str, subString: str):
    arquivos = glob.glob(pasta + "\\*")
    arquivosFiltrados = filter(lambda x: subString in x, arquivos)
    return arquivosFiltrados
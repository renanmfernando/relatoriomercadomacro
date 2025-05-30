import os
from util.LagunaAPI import log
from enum import Enum

class Servico():
    loginLaguna = "LoginLaguna"
    webServicePassivo = "WebServicePassivo"
    institucionalXP = "InstitucionalXP"

def getUsuarioLaguna() -> str:
    return getPalavra(True, Servico.loginLaguna)

def getSenhaLaguna() -> str:
    return getPalavra(False, Servico.loginLaguna)

def getUsuarioWebServicePassivo() -> str:
    return getPalavra(True, Servico.webServicePassivo)

def getSenhaWebServicePassivo() -> str:
    return getPalavra(False, Servico.webServicePassivo)

def getUsuarioInstitucionalXP() -> str:
    return getPalavra(True, Servico.institucionalXP)

def getSenhaInstitucionalXP() -> str:
    return getPalavra(False, Servico.institucionalXP)

def getPalavra(pegarUsuario: bool ,nomeServico: str) -> str:

    indexPalavra = 1
    if pegarUsuario == False: 
        indexPalavra = 2 

    try:
        
        path=os.path.expanduser("~\\documents\\LagunaConfig\\logins.txt")
        streamPath = open(path)
        linhas = streamPath.readlines()

        for linha in linhas:
            if linha.startswith(nomeServico):
                palavras = linha.rsplit(',')
                return palavras[indexPalavra]

    except:
        msg = 'Importador Arquivos Intrag: Não foi possível obter credenciais de Documents'
        log(msg)
        raise Exception(msg)
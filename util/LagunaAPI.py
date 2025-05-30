import os, requests, json
from datetime import datetime
from typing import List

# CaminhoServico = "http://localhost:59396/"
# CaminhoServico = "http://ventorws01/lagunaservicotestes/"
CaminhoServico = "http://ventorws01/lagunaservico/"

def getDmenos1() -> datetime:
    respostaStr = getAPIanonimo('calendario', 'D-1')
    return converteDataWebAPI(respostaStr)

def diaUtil(data: datetime, numDias: int) -> datetime:
    dataStr = data.strftime('%Y-%m-%d')
    respostaStr = getAPIanonimo('calendario', 'diautil', 'data', dataStr, 'numdias', str(numDias))
    return converteDataWebAPI(respostaStr)

def isDiaUtil(data: datetime) -> bool:
    dataStr = data.strftime('%Y-%m-%d')
    meuBoolStr = getAPIanonimo('calendario', 'isdiautil', 'data', dataStr)
    meuBool = json.loads(meuBoolStr)
    return meuBool

def log(mensagem: str):
    postAPIanonimo('logger', 'log', 'mensagem', mensagem)

def logErro(mensagem: str):
    postAPIanonimo('logger', 'logerro', 'mensagem', mensagem.strip())

def logTerminal(mensagem: str):
    postAPIanonimo('logger', 'logterminal', 'mensagem', mensagem)

def logErroTerminal(mensagem: str):
    postAPIanonimo('logger', 'logerroterminal', 'mensagem', mensagem.strip())

def logScript(mensagem: str):
    postAPIanonimo('logger', 'logScript', 'mensagem', mensagem)

def logErroScript(mensagem: str):
    postAPIanonimo('logger', 'logerroscript', 'mensagem', mensagem.strip())

def getAPIanonimo(controller, funcao, nomeParam1='', valorParam1='',
           nomeParam2='', valorParam2='',
           nomeParam3='', valorParam3='',
           nomeParam4='', valorParam4=''):

    caminho = CaminhoServico + "api/" + controller + "/" + funcao

    if nomeParam1 != '':
        caminho += "?" + nomeParam1 + "=" + valorParam1

    if nomeParam2 != '':
        caminho += "&" + nomeParam2 + "=" + valorParam2

    if nomeParam3 != '':
        caminho += "&" + nomeParam3 + "=" + valorParam3

    if nomeParam4 != '':
        caminho += "&" + nomeParam4 + "=" + valorParam4

    resposta = requests.get(caminho)
    return resposta.content

def getValorDeParametro(nomeParametro: str) -> str:
    valor = getRespostaAPI('parametro', 'Parametro', 'nome', nomeParametro)

    valorStr : str = valor.json()

    return valorStr

def getRespostaAPI(controller, funcao, nomeParam1='', valorParam1='',
           nomeParam2='', valorParam2=''):

    caminho = CaminhoServico + "api/" + controller + "/" + funcao

    if nomeParam1 != '':
        caminho += "?" + nomeParam1 + "=" + valorParam1

    if nomeParam2 != '':
        caminho += "&" + nomeParam2 + "=" + valorParam2

    token = getToken()

    headers = {}
    headers["Authorization"] = "Bearer " + token

    resposta = requests.get(caminho, headers=headers)
    return resposta

def getAPI(controller, funcao, nomeParam1='', valorParam1='',
           nomeParam2='', valorParam2=''):

    resposta = getRespostaAPI(controller, funcao, nomeParam1, valorParam1, nomeParam2, valorParam2)
    return resposta.content


def postAPI(controller, funcao, nomeParam='', valorParam='',
                                nomeParam2='', valorParam2='',
                                nomeParam3='', valorParam3='',
                                nomeParam4='', valorParam4='',
                                nomeParam5='', valorParam5='',
                                nomeParam6='', valorParam6='',
                                nomeParam7='', valorParam7='',
                                nomeParam8='', valorParam8=''):

    caminho = CaminhoServico + "api/" + controller + "/" + funcao
    if nomeParam != '':
        caminho += "?" + nomeParam + "=" + valorParam

    if nomeParam2 != '':
        caminho += "&" + nomeParam2 + "=" + valorParam2

    if nomeParam3 != '':
        caminho += "&" + nomeParam3 + "=" + valorParam3

    if nomeParam4 != '':
        caminho += "&" + nomeParam4 + "=" + valorParam4

    if nomeParam5 != '':
        caminho += "&" + nomeParam5 + "=" + valorParam5

    if nomeParam6 != '':
        caminho += "&" + nomeParam6 + "=" + valorParam6

    if nomeParam7 != '':
        caminho += "&" + nomeParam7 + "=" + valorParam7

    if nomeParam8 != '':
        caminho += "&" + nomeParam8 + "=" + valorParam8

    token = getToken()

    headers = {}
    headers["Authorization"] = "Bearer " + token

    resposta = requests.post(caminho, None, headers=headers)
    return resposta.content

def postAPIanonimo(controller, funcao, nomeParam='', valorParam='',
                                nomeParam2='',  valorParam2='',
                                nomeParam3='',  valorParam3='',
                                nomeParam4='',  valorParam4='',
                                nomeParam5='',  valorParam5='',
                                nomeParam6='',  valorParam6='',
                                nomeParam7='',  valorParam7='',
                                nomeParam8='',  valorParam8='',
                                nomeParam9='',  valorParam9='',
                                nomeParam10='', valorParam10='',
                                nomeParam11='', valorParam11='',
                                nomeParam12='', valorParam12=''):

    caminho = CaminhoServico + "api/" + controller + "/" + funcao
    if nomeParam != '':
        caminho += "?" + nomeParam + "=" + valorParam

    if nomeParam2 != '':
        caminho += "&" + nomeParam2 + "=" + valorParam2

    if nomeParam3 != '':
        caminho += "&" + nomeParam3 + "=" + valorParam3

    if nomeParam4 != '':
        caminho += "&" + nomeParam4 + "=" + valorParam4

    if nomeParam5 != '':
        caminho += "&" + nomeParam5 + "=" + valorParam5

    if nomeParam6 != '':
        caminho += "&" + nomeParam6 + "=" + valorParam6

    if nomeParam7 != '':
        caminho += "&" + nomeParam7 + "=" + valorParam7

    if nomeParam8 != '':
        caminho += "&" + nomeParam8 + "=" + valorParam8

    if nomeParam9 != '':
        caminho += "&" + nomeParam9 + "=" + valorParam9
        
    if nomeParam10 != '':
        caminho += "&" + nomeParam10 + "=" + valorParam10
        
    if nomeParam11 != '':
        caminho += "&" + nomeParam11 + "=" + valorParam11
        
    if nomeParam12 != '':
        caminho += "&" + nomeParam12 + "=" + valorParam12

    resposta = requests.post(caminho)
    return resposta.json()

def postAPIjson(controller, funcao, dados, nomeParam ='', valorParam ='',
                                           nomeParam1 ='', valorParam1 =''):

    caminho = CaminhoServico + "api/" + controller + "/" + funcao
    if nomeParam != '':
        caminho += "?" + nomeParam + "=" + valorParam

    if nomeParam1 != '':
        caminho += "&" + nomeParam1 + "=" + valorParam1

    resposta = requests.post(caminho,  json = dados)
    return resposta.json()

def getToken():

    pastaUsuario = os.path.expanduser('~')
    caminhoCredenciais = os.path.join(
        pastaUsuario, 'Documents\\LagunaConfig\\logins.txt')

    arquivoCredenciais = open(caminhoCredenciais, 'r')

    linhas = arquivoCredenciais.readlines()
    for linha in linhas:
        if str(linha).strip().startswith('LoginLaguna'):
            usuario = str(linha).rsplit(',')[1]
            senha = str(linha).rsplit(',')[2]

    senha = senha.strip('\n')

    endpoint = CaminhoServico + "/token"

    header = {}
    header["Content-Type"] = "application/x-www-form-urlencoded"

    dados = {}
    dados["grant_type"] = "password"
    dados["username"] = usuario
    dados["password"] = senha

    resposta = requests.post(endpoint, dados)

    return resposta.json()['access_token']


def converteDataWebAPI(dataWebAPI) -> datetime:

    dataStr = str(dataWebAPI).split('T')[0]
    dataStr = dataStr.replace('b','')
    dataStr = dataStr.replace('\\','')
    dataStr = dataStr.replace('"','')
    dataStr = dataStr.replace('\'','')
    dataObj = datetime.strptime(dataStr, '%Y-%m-%d')
    return dataObj
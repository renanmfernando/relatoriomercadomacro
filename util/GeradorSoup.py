import requests
from bs4 import BeautifulSoup

def getSoup(url):

    headers = {"User-Agent":"Mozilla/5.0"}
    bla = requests.get(url, headers=headers)
    meuhtml =  bla.content
    soup = BeautifulSoup(meuhtml, 'html.parser')
    return soup

def getSoupDeArquivoHtml(caminho):

    try:
        arquivo = open(caminho, encoding="utf8")
        conteudo = arquivo.read()
    except:
        arquivo = open(caminho)
        conteudo = arquivo.read()

    soup = BeautifulSoup(conteudo, 'html.parser')
    return soup
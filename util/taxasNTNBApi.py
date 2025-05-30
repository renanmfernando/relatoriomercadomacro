from asyncore import read
import locale, time
from datetime import datetime

from pandas import read_clipboard
from LagunaAPI import getAPIanonimo, postAPIanonimo

def converteValor(valorStr: str) -> float:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.atof(valorStr)

def converteMes(vencimento):
    ano = vencimento[-2:]
    ano =int(ano)
    if ano % 2 == 0:
        mes = "AGO/"+str(ano)
    if ano % 2 != 0:
        mes = "MAI/"+str(ano)
    return mes 

input('Aperte ENTER após copiar taxas com CTRL+C :')

strTaxas = read_clipboard()
strTaxas = str(strTaxas)
listaTaxas = strTaxas.splitlines()

dataHoje =  datetime.today()
dataStr = dataHoje.strftime('%Y-%m-%d') 

for linha in listaTaxas:
    linha = linha[4:]
    linha = linha.split(' ')
    vencimento = linha[0].upper()
    
    taxaStr = linha[2]
    taxaStr = taxaStr.replace('%', '')
    taxa: float = converteValor(taxaStr)
    taxaStr = str(taxa)

    if 'ago' in linha[0]:
        nome = "NTN-B" + " " + str(vencimento)
    else:
        nome = "NTN-B" + " " + converteMes(vencimento)    
        
    idAtivoBytes = getAPIanonimo('ativo', 'getId', 'nome', nome)

    idAtivoStr = idAtivoBytes.decode()

    retorno = postAPIanonimo('DadoAtivo', 'insereDadoDeAtivo','dado', 'TaxaIndicativa', 'idAtivo', idAtivoStr, 'data', dataStr, 'valor', taxaStr)
    
    print(retorno)

time.sleep(5)
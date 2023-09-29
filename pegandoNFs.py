import os
import re

diretorio = r'C:\Users\70094757178\Documents\Leandro\Nfs\Parts'

arquivos = os.listdir(diretorio)
numNotasFiscais = []
nomeArquivoNf = []

for arquivo in arquivos:
    nomeArquivoNf.append(arquivo)

    nf= arquivo[0:10]                                                                     # Pega os 9 primeiros caracteres da string
    nf= re.sub(r'[\sA-za-z]*','',nf)                                          # Tira todos os espacos em branco e todas as letras da pagina
    numNotasFiscais.append(nf)                                                            # Coloca o numero da nota no array


print(nomeArquivoNf)
print(numNotasFiscais)
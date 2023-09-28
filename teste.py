import os

diretorio = r'\\CEMEV_SUECG01\Becape do Rececimento\Recebimento 2023\PARTS LUB\RP 38'

arquivos = os.listdir(diretorio)

for arquivo in arquivos:
    print(arquivo)
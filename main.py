from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import re
import time

# Iniciando o driver
driver = webdriver.Firefox()

# Acessando o Sei
driver.get("https://sei.df.gov.br/sip/login.php?sigla_orgao_sistema=GDF&sigla_sistema=SEI")


# Descobrindo os tags Html do login do SEI
btnAcessarLogin = driver.find_element(By.ID,'sbmLogin')
usuarioField = driver.find_element(By.ID,'txtUsuario')
senhaField = driver.find_element(By.ID,'pwdSenha')
orgaoField = driver.find_element(by=By.ID,value='selOrgao')

# Preenchendo formulario de login
usuarioField.send_keys('3061867')
senhaField.send_keys('contrato00@')
orgaoField.send_keys('CBMDF')
btnAcessarLogin.click()

# Fechando pop-up
janelasAbertas = driver.window_handles                                            # Pegando todas as janelas do mozila abertas
driver.switch_to.window(janelasAbertas[1])                                        # O popUp é a segunda Janela
driver.close()                                                                    # Fechando o popUp
driver.switch_to.window(janelasAbertas[0])                                        # Voltando para a Tela principal

# Selecionando SELOG
selogSelectTag = driver.find_element(By.NAME,'selInfraUnidades')            # Acha a tag <select> HTML
select = Select(selogSelectTag)                                                   # Transforma em Select - uma classe do Selenium
select.select_by_visible_text('CBMDF/CEMEV/SELOG')                                # Abre a Selog

# Acessando o processo
pesquisaProceso = driver.find_element(By.ID,'txtPesquisaRapida')            # Seleciona o campo de busca no SEI

nomeEmpresa = 'parts'

if nomeEmpresa in 'parts lub':                                                    # Criando uma estruta para as 4 empresas possiveis
    pesquisaProceso.send_keys('00053-00099475/2021-17')
    pesquisaProceso.send_keys(Keys.ENTER)


elif nomeEmpresa in 'robson':
    pesquisaProceso.send_keys('00053-00099470/2021-94')
    pesquisaProceso.send_keys(Keys.ENTER)

elif nomeEmpresa in 'gilson rabelo':
    pesquisaProceso.send_keys('00053-00137744/2022-31')
    pesquisaProceso.send_keys(Keys.ENTER)

elif nomeEmpresa in 'alberto':
    pesquisaProceso.send_keys('00053-00099465/2021-81')
    pesquisaProceso.send_keys(Keys.ENTER)


# ACESSANDO A ULTIMA RP DE MANUTENCAO DE VEICULOS
time.sleep(5)                                                                 # Espera 5 segundos ate a pagina carregar
page_source = driver.page_source                                              # Pega Html da pagina inteira

iframeArvore = driver.find_element(By.ID,'ifrArvore')                   # Pega o <iframe> arvore que contem os processos relacionados dentro
driver.switch_to.frame(iframeArvore)                                          # Muda para o iframe 'ifrArvore'

manutencaoVeiculos = driver.find_element(By.PARTIAL_LINK_TEXT,'Manutenção')                                                                 # Pega a tag que contem o texto manutencao
ultimaRp = driver.find_element(By.XPATH,'//a[contains(text(),"Manutenção")]/following-sibling::*[2]/br[last()]/preceding-sibling::*[1]')    # Acha a ultima Rp seguindo esse paço html
processoUltimaRp = ultimaRp.get_attribute('textContent')                                                                                          # Pega o texto da tag da ultima Rp que é o processo SEI
driver.switch_to.default_content()

pesquisaProceso = driver.find_element(By.ID,'txtPesquisaRapida')                                                                            # Acha a barra de pesquisa
pesquisaProceso.send_keys(processoUltimaRp)                                                                                                       # Preenche a pesquisa com o processo SEI da ultima RP
pesquisaProceso.send_keys(Keys.ENTER)


# PEGANDO OS DADOS DA ULTIMA RP (NUMERO DA RP ANTIGA)
# time.sleep(5)
# iframeVisualizacao = driver.find_element(By.ID,'ifrVisualizacao')                                       # Pega o <iframe> Visualizacao que contem o icone de alterar documento dentro
# driver.switch_to.frame(iframeVisualizacao)                                                                    # Muda para o iframe 'Visualizacao
# iconeBoneco =  driver.find_element(By.XPATH,'//img[contains(@title,"Alterar Processo")]/..')            # Acha o icone Boneco
# iconeBoneco.click()                                                                                           # Clica no icone Boneco
#
# tagNRP = driver.find_element(By.ID,'txtDescricao')                                                      # Encontra o campo input que esta o numero da RP
# nRp = tagNRP.get_attribute('value')                                                                           # Pega o valor do campo input
# nRp = re.sub(r'\/\d{2,4}','',nRp)                                                                 # Formata a string para conter somente o numero
# nRp = re.sub(r'[\sa-zA-z]*','',nRp)
#
# print(f'ultima Rp: {nRp}')
#
# driver.switch_to.default_content()                                                                            # Volta para o Html principal
# pesquisaProceso = driver.find_element(By.ID,'txtPesquisaRapida')                                        # Acha o campo pesquisa
# pesquisaProceso.send_keys(processoUltimaRp)                                                                   # Preenche a pesquisa com o processo SEI da ultima RP
# pesquisaProceso.send_keys(Keys.ENTER)

# DUPLICA A ULTIMA RP
# time.sleep(5)
# iframeVisualizacao = driver.find_element(By.ID,'ifrVisualizacao')                                       # Pega o <iframe> Visualizacao que contem o icone de alterar documento dentro
# driver.switch_to.frame(iframeVisualizacao)                                                                    # Muda para o iframe 'Visualizacao
# iconeBoneco =  driver.find_element(By.XPATH,'//img[contains(@title,"Duplicar Processo")]/..')           # Acha o icone Boneco
# iconeBoneco.click()
#
# checkManterRelacionamento = driver.find_element(By.ID,'chkSinProcessosRelacionados')                    # Acha o botao que mantem os relacionamentos
# checkManterRelacionamento.click()
#
#
# for indice, inputCheck in enumerate(range(40,14, -1)):
#     try:
#         inputCheck = driver.find_element(By.ID,f'chkInfraItem{40-indice}')
#         inputCheck.click()
#     except:
#         print(f'nao encontrado check {40-indice} ]')
#
# btnDuplicarProcesso = driver.find_element(By.ID,'btnDuplicarProcesso')
# btnDuplicarProcesso.click()

# EDITAR RP CRIADA
time.sleep(5)
iframeArvore = driver.find_element(By.ID,'ifrArvore')                   # Pega o <iframe> arvore que contem os processos relacionados dentro
driver.switch_to.frame(iframeArvore)


    # Primeira NF
nf1 = driver.find_element(By.XPATH,'//span[contains(text(),"Nota Fiscal")]/..')
nf1.click()

driver.switch_to.default_content()
iframeVisualizacao = driver.find_element(By.ID,'ifrVisualizacao')                                       # Pega o <iframe> Visualizacao que contem o icone de alterar documento dentro
driver.switch_to.frame(iframeVisualizacao)

iconeBoneco =  driver.find_element(By.XPATH,'//img[contains(@title,"Alterar Documento Externo")]/..')            # Acha o icone Boneco da NF
iconeBoneco.click()

uploadNf1 =  driver.find_element(By.ID,'filArquivo')
uploadNf1.send_keys(r'\\CEMEV_SUECG01\Becape do Rececimento\Recebimento 2023\PARTS LUB\RP 38\NF 4200 PED 1829.pdf')
time.sleep(3)

btnSalvar = driver.find_element(By.ID,'btnSalvar')
btnSalvar.click()

    # Segunda NF

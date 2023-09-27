from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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

nomeEmpresa = 'Parts Lub'                                                         # Seleciona o nome da empresa a ser pesquisa no SEI
nomeEmpresa = nomeEmpresa.lower()

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

# processosRelacionados = driver.find_element(By.ID,'divRelacionadosParciais')
# print(processosRelacionados.text)
# ultimaRp = driver.find_element(By.XPATH,"//a[contains(text(),'Gest')]")
# ultimRp.click()

# print(processoLink)





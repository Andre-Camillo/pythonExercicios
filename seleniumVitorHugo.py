
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
sleep(60)

def bot():
    try:
        bolinha = driver.find_element_by_class_name('_1pJ9J')
        bolinha = driver.find_elements_by_class_name('_1pJ9J')
        clica_bolinha = bolinha[- 1]
        acao_bolinha = webdriver.common.action_chains.ActionChains(driver)
        acao_bolinha.move_to_elemente_with_offset(clica_bolinha, 0, -20)
        acao_bolinha.click()
        acao_bolinha.perform()
        acao_bolinha.click()
        acao_bolinha.perform()

    except:
        print('buscando novas mensagens')
        sleep(3)
while True:
    bot()

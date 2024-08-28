# 27/08/2024 18:10 - 19:11 Preparacao do ambiente

# requests ou selenium (selenium)

# Documentação Selenium
# https://selenium-python.readthedocs.io/locating-elements.html

# Escolha do navegador
# https://gs.statcounter.com/browser-market-share
# Chrome 65.41% Safari 18.39% Edge 5.24% Firefox 2.74% Samsung Internet 2.59% Opera 2.06%

# Entrar na página de login

# https://2captcha.com/api-docs/recaptcha-v2
# https://sites.google.com/chromium.org/driver/downloads
# https://googlechromelabs.github.io/chrome-for-testing/#stable

# pip uninstall TwoCaptcha
# pip install 2captcha-python

# https://github.com/2captcha/2captcha-python?tab=readme-ov-file#recaptcha-v2
# https://2captcha.com/demo/recaptcha-v2
# https://2captcha.com/2captcha-api#solving_recaptchav2_new
# https://2captcha.com/api-docs/recaptcha-v2

# Importacoes
# Importacoes 1
from secret import secret_cemig
from secret import secret_2captcha
import time
# Importacoes 2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# Importacoes 3
from twocaptcha import TwoCaptcha

driver = None
def login():
    global driver
    paginalogin = "https://atende.cemig.com.br/Login"
    # Login pagina
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(paginalogin)
    time.sleep(5)
    # Login cookies
    cookies_off = driver.find_element(By.XPATH, '//*[@id="onetrust-reject-all-handler"]')
    if cookies_off.is_enabled():
        cookies_off.click()
    time.sleep(2)
    # Login usuario
    usuario = driver.find_element(By.XPATH, '//*[@id="acesso"]')
    usuario.send_keys(secret_cemig['usuario'])
    time.sleep(2)
    # Login senha
    senha = driver.find_element(By.XPATH, '//*[@id="senha"]')
    senha.send_keys(secret_cemig['senha'])
    time.sleep(2)
    # Login captcha
    grecaptcha = driver.find_element(By.XPATH, '//*[@class="g-recaptcha"]')
    datasitekey = grecaptcha.get_attribute('data-sitekey')
    solver = TwoCaptcha(secret_2captcha['key'])
    result = solver.recaptcha(sitekey=datasitekey,url=paginalogin)
    grecaptcharesponse = driver.find_element(By.XPATH, '//*[@class="g-recaptcha-response"]')
    driver.execute_script("arguments[0].style.display = 'block';", grecaptcharesponse)
    grecaptcharesponse.send_keys(result['code'])
    # Login final
    submit = driver.find_element(By.XPATH, '//*[@id="submitForm"]')
    submit.click()
    time.sleep(5)

def segundavia():
    global driver
    paginasegundavia = "https://atende.cemig.com.br/SegundaVia"
    # Segundavia pagina
    driver.get(paginasegundavia)
    time.sleep(5)
    # Segundavia download
    tabela = driver.find_elements(By.XPATH, '//*[@id="tblGrid"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", tabela)
    contas = driver.find_elements(By.XPATH, '//*[@id="tblGrid"]/tbody/tr')
    if contas:
        for conta in contas:
            download = conta.find_element(By.XPATH, './td[8]/div/a/span[1]')
            driver.execute_script("arguments[0].scrollIntoView(true);", download)
            download.click()
            time.sleep(5)

def sair():
    # Saida
    global driver
    perfil = driver.find_element(By.XPATH, '//*[@id="dropdownUsuarioMenu"]/a/span/i[1]')
    perfil.click()
    time.sleep(2)
    sair = driver.find_element(By.XPATH, '//*[@id="dropdownUsuarioMenu"]/ul/li[6]/a')
    sair.click()
    time.sleep(2)
    driver.close()

login()
segundavia()
sair()

#tipo de captcha muda de acordo com frequencia de logins
#id="captchaImg" src="data:image/png;base64,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"
#class="g-recaptcha" data-sitekey="6Lel5yQTAAAAAL3DDXn2lm6J31ke4awM587E001a"










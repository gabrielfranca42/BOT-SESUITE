from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

URL = "https://suape-test.softexpert.com/softexpert/login?page=12,129"
USUARIO = ""
SENHA = ""


options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

print("Abrindo site...")
driver.get(URL)

print("Digitando usuário...")
wait.until(EC.presence_of_element_located((By.ID, "user"))).send_keys(USUARIO)

print("Digitando senha...")
wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(SENHA)

print("Enviando login...")
wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(Keys.ENTER)

time.sleep(5)

# ===== POPUP =====
try:
    print("Verificando popup...")
    ok_button = wait.until(
        EC.element_to_be_clickable((By.ID, "alertConfirm"))
    )
    print("Popup encontrado, clicando OK...")
    ok_button.click()
    time.sleep(3)
except:
    print("Nenhum popup encontrado.")

# ===== COMPONENTES =====
print("Aguardando botão Componentes...")

componentes = wait.until(
    EC.element_to_be_clickable((By.ID, "components"))
)

print("Clicando no botão Componentes...")
componentes.click()

print("Sucesso! Menu aberto.")

time.sleep(10)
driver.quit()


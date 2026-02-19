from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time
import sys

URL = "https://suape-test.softexpert.com/softexpert/login?page=12,129"
USUARIO = "gabrielfranca"
SENHA = "290504gE110621g@"

options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 40)

try:
    print("===== INICIANDO SCRIPT =====")

    print("Abrindo site...")
    driver.get(URL)

    # ALTERADO: Espera documento completamente carregado
    print("Aguardando página carregar completamente...")
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    print("Digitando usuário...")
    wait.until(EC.presence_of_element_located((By.ID, "user"))).send_keys(USUARIO)

    print("Digitando senha...")
    driver.find_element(By.ID, "password").send_keys(SENHA)

    print("Enviando login...")
    driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

    print("Aguardando carregamento pós login...")
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    time.sleep(4)

    # ===== POPUP =====
    try:
        print("Verificando popup...")
        popup = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "alertConfirm"))
        )
        print("Popup encontrado. Clicando...")
        popup.click()

        # ALTERADO: espera popup sumir
        wait.until(EC.invisibility_of_element_located((By.ID, "alertConfirm")))
        print("Popup fechado com sucesso.")

    except TimeoutException:
        print("Nenhum popup encontrado.")

    print("Procurando botão Components...")

    # ALTERADO: espera elemento existir
    components_button = wait.until(
        EC.presence_of_element_located((By.ID, "components"))
    )

    # ALTERADO: scroll até o elemento
    print("Scrollando até o botão...")
    driver.execute_script("arguments[0].scrollIntoView(true);", components_button)
    time.sleep(2)

    # ALTERADO: espera visibilidade real
    wait.until(EC.visibility_of(components_button))
    wait.until(EC.element_to_be_clickable((By.ID, "components")))

    print("Executando hover...")
    ActionChains(driver).move_to_element(components_button).perform()
    time.sleep(2)

    print("Tentando clique normal...")
    try:
        components_button.click()
    except Exception:
        print("Clique normal falhou. Tentando clique via JavaScript...")
        driver.execute_script("arguments[0].click();", components_button)

    print("Clique executado.")

    # ALTERADO: espera drawer aparecer corretamente
    print("Aguardando menu abrir...")
    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "drawerSideBar"))
    )

    print("Menu de Componentes abriu com sucesso.")

    print("Aguardando 20 segundos antes de fechar...")
    time.sleep(20)

except Exception as e:
    print("ERRO CRÍTICO:", e)
    sys.exit(1)

finally:
    print("Encerrando navegador...")
    driver.quit()
    print("===== SCRIPT FINALIZADO =====")

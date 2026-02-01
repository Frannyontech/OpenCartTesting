from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException, StaleElementReferenceException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By



class BasePage:
    def __init__(self, driver):
        self.driver = driver

#asserts: abrir, esperar_elemento_clickable,  doble_click, esperar_visibilidad, esperar_elemento_clickable, escribir(send_keys), tab, obtener_texto

    def open(self, url):
        self.driver.get(url)

    def esperar_carga_completa(self, locator, timeout=120):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Elemento no visible después de {timeout}s: {locator}")

    def esperar_elemento_clickable(self, locator, timeout=120):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Elemento no clickeable después de {timeout}s: {locator}")

    def tab(self):
        ActionChains(self.driver).send_keys("\t").perform()

    def set_text(self, locator, texto, timeout=10):
        ele = self.esperar_carga_completa(locator, timeout)
        ele.clear()
        ele.send_keys(texto)

    def obtener_texto(self, locator, timeout=10):
        try:
            elemento = self.esperar_carga_completa(locator, timeout)
            texto = elemento.text or ""
        except (TimeoutException, StaleElementReferenceException):
            return None
        texto = texto.replace("\xa0", " ")
        texto = " ".join(texto.split())
        return texto if texto else None

    def seleccionar_opcion(self, locator_select, texto):
        select = Select(self.esperar_carga_completa(locator_select))
        select.select_by_visible_text(texto)


    def click_seguro(self, locator, timeout=120):
        ele = self.esperar_elemento_clickable(locator, timeout)
        # scrollea como js
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", ele
        )
        try:
            ele.click()
        except WebDriverException:
            # fallback por JS
            self.driver.execute_script("arguments[0].click();", ele)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage

#pagina de inicio del ecommerce

class HomePage_SearchPage(BasePage):
#locators
    locators = {
        "input_buscar": (By.NAME, 'search'),
        "btn_buscar": (By.CLASS_NAME, 'btn-default'),
        "select_resultados": (By.CLASS_NAME, 'product-thumb'),
        "select_primer_producto": (By.XPATH, '//*[@id="content"]/div[3]/div[1]'),
        "txt_titulo_producto": (By.XPATH, '//*[@id="content"]/div[1]/div[2]/h1'),
        "txt_precio_producto": (By.XPATH, '//*[@id="content"]/div[1]/div[2]/ul[2]/li[1]/h2')
    }

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(15)
        super().__init__(driver)

    def buscar_producto(self, nombre_producto):
        self.esperar_carga_completa(self.locators["input_buscar"])
        self.set_text(self.locators["input_buscar"], nombre_producto)
        self.esperar_elemento_clickable(self.locators["btn_buscar"]).click()
        self.esperar_carga_completa(self.locators["select_resultados"])
        self.esperar_elemento_clickable(self.locators["select_primer_producto"]).click()


    def obtener_informacion_producto(self):
        nombre = self.obtener_texto(self.locators["txt_titulo_producto"])
        precio = self.obtener_texto(self.locators["txt_precio_producto"])

        print(f"Producto encontrado: {nombre}")
        print(f"Precio del producto: {precio}")

        
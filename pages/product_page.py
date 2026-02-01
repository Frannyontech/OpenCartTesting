import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage

#agregar a carrito

class HomePage_ProductPage(BasePage):
#locators
    locators = {
        "select_producto": (By.XPATH, '//*[@id="content"]/div[2]/div[4]/div'),
        "txt_titulo_producto": (By.XPATH, '//*[@id="content"]/div/div[2]/h1'),
        "txt_precio_producto": (By.XPATH, '//*[@id="content"]/div/div[2]/ul[2]/li[2]/h2'),
        "select_color": (By.ID, 'input-option226'),
        "option_color": (By.XPATH, '//*[@id="input-option226"]/option[3]'),
        "btn_agregar_carrito": (By.ID, 'button-cart'),
        "txt_confirmar": (By.CLASS_NAME, 'alert-success')
    }

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def buscar_producto(self):
        self.esperar_carga_completa(self.locators["select_producto"])
        print(f"elemento encontrado")
        self.esperar_elemento_clickable(self.locators["select_producto"]).click()

    def obtener_informacion_producto(self):
        time.sleep(10)
        nombre = self.obtener_texto(self.locators["txt_titulo_producto"])
        precio = self.obtener_texto(self.locators["txt_precio_producto"])

        print(f"Producto encontrado: {nombre}")
        print(f"Precio del producto: {precio}")

    def agregar_carro_compras(self):
        self.esperar_elemento_clickable(self.locators["select_color"]).click()
        self.esperar_elemento_clickable(self.locators["option_color"]).click()     
        self.esperar_elemento_clickable(self.locators["btn_agregar_carrito"]).click()  

        txt_exitoso = self.obtener_texto(self.locators["txt_confirmar"])
        print(f"Proceso exitoso: {txt_exitoso}")
        
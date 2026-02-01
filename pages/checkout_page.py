import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage

#agregar a carrito

class HomePage_CheckoutPage(BasePage):
#locators
    locators = {
        "select_producto": (By.CLASS_NAME, "swiper-viewport"),
        "btn_agregar_carrito": (By.ID, 'button-cart'),
        "btn_carro": (By.ID, 'cart'),
        "btn_checkout": (By.XPATH, '//*[@id="cart"]/ul/li[2]/div/p/a[2]'),
        "option_invitado": (By.XPATH, '//*[@id="collapse-checkout-option"]/div/div/div[1]/div[2]/label/input'),
        "btn_continuar_invitado": (By.ID, 'button-account'),
        "txt_nombre": (By.ID, 'input-payment-firstname'),
        "txt_apellido": (By.ID, 'input-payment-lastname'),
        "txt_email": (By.ID, 'input-payment-email'),
        "txt_telefono": (By.ID, 'input-payment-telephone'),
        "txt_direccion": (By.ID, 'input-payment-address-1'),
        "txt_ciudad": (By.ID, 'input-payment-city'),
        "txt_codigo_postal": (By.ID, 'input-payment-postcode'),
        "select_pais": (By.ID, 'input-payment-country'),
        "select_region": (By.ID, 'input-payment-zone'),
        "btn_continuar_detalle": (By.ID, 'button-guest'),
        "btn_continuar_envio": (By.ID, 'button-shipping-method'),
        "checkbox_metodo_pago": (By.XPATH, '//*[@id="collapse-payment-method"]/div/div[3]/div/input[1]'),
        "btn_continuar_pago": (By.ID, 'button-payment-method'),
        "btn_confirmar_orden": (By.ID, 'button-confirm'),
        "txt_exitoso": (By.XPATH, '//*[@id="content"]/h1'),
        "btn_continuar": (By.CLASS_NAME, 'btn-primary')
    }

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def buscar_producto(self):
        self.esperar_elemento_clickable(self.locators["select_producto"]).click()

    def agregar_carro_compras(self):  
        self.esperar_carga_completa(self.locators["btn_agregar_carrito"])
        self.esperar_elemento_clickable(self.locators["btn_agregar_carrito"]).click()
        self.esperar_elemento_clickable(self.locators["btn_carro"]).click()
        self.esperar_elemento_clickable(self.locators["btn_checkout"]).click()

    def checkout(self, nombre, apellido, email, telefono, direccion, ciudad, codigo_postal, pais, region):
        self.esperar_elemento_clickable(self.locators["option_invitado"]).click()
        self.esperar_elemento_clickable(self.locators["btn_continuar_invitado"]).click()
        self.set_text(self.locators["txt_nombre"], nombre)
        self.set_text(self.locators["txt_apellido"], apellido)
        self.set_text(self.locators["txt_email"], email)
        self.set_text(self.locators["txt_telefono"], telefono)
        self.set_text(self.locators["txt_direccion"], direccion)
        self.set_text(self.locators["txt_ciudad"], ciudad)
        self.set_text(self.locators["txt_codigo_postal"], codigo_postal)
        self.seleccionar_opcion(self.locators["select_pais"], pais)
        time.sleep(2)
        self.seleccionar_opcion(self.locators["select_region"], region)
        self.click_seguro(self.locators["btn_continuar_detalle"])
        time.sleep(3)
        self.click_seguro(self.locators["btn_continuar_envio"])
        self.esperar_elemento_clickable(self.locators["checkbox_metodo_pago"]).click()
        self.click_seguro(self.locators["btn_continuar_pago"])
        self.click_seguro(self.locators["btn_confirmar_orden"])

        txt_exitoso = self.obtener_texto(self.locators["txt_exitoso"])
        print(f"Proceso exitoso: {txt_exitoso}")

        self.esperar_elemento_clickable(self.locators["btn_continuar"]).click()

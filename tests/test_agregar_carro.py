import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.product_page import HomePage_ProductPage


def test_agregar_producto_carro(base_url, driver):
    driver.get(base_url)
    home_page_nuevo = HomePage_ProductPage(driver)

    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors=yes")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    home_page_nuevo.buscar_producto()
    home_page_nuevo.obtener_informacion_producto()
    home_page_nuevo.agregar_carro_compras()
    time.sleep(5)
    driver.quit()
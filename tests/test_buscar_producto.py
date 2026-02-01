import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage_SearchPage


def test_buscar_producto(base_url, driver):
    #variables de busqueda
    nombre_producto = "mac"

    driver.get(base_url)
    home_page_nuevo = HomePage_SearchPage(driver)
    home_page_nuevo.buscar_producto(nombre_producto)
    home_page_nuevo.obtener_informacion_producto()
    
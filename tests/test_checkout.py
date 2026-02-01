import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.checkout_page import HomePage_CheckoutPage


def test_checkout(base_url, driver):
    #variables de busqueda
    nombre = "francisca"
    apellido = "galaz"
    email = "correo@correo.com"
    telefono = "999999999"
    direccion = "Avenida Andrés Bello 2425"
    ciudad = "providencia"
    codigo_postal = "76572527"
    pais = "Chile"
    region = "Region Metropolitana"

    driver.get(base_url)
    home_page_nuevo = HomePage_CheckoutPage(driver)

    home_page_nuevo.buscar_producto()
    home_page_nuevo.agregar_carro_compras()
    home_page_nuevo.checkout(nombre, apellido, email, telefono, direccion, ciudad, codigo_postal, pais, region)

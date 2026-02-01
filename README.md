# Desafio Tecnico - Automating OpenCart

Este proyecto corresponde a un desafío técnico de automatización End-to-End sobre un ecommerce basado en **OpenCart**, desarrollado en **Python** utilizando **Selenium WebDriver**, **Pytest** y el patrón **Page Object Model (POM)**

El objetivo fue validar flujos críticos del sistema

---

## Casos de prueba implementados y cobertura

Se automatizaron **tres flujos relevantes**, representativos del comportamiento real de un usuario cliente:

1. **Búsqueda de producto**
   - Ingreso al sitio
   - Búsqueda por texto
   - Selección de producto desde resultados
   - Captura de evidencia (screenshot)

2. **Agregar producto al carrito**
   - Navegación al detalle del producto
   - Agregado correcto al carro de compras
   - Captura de evidencia (screenshot)  

3. **Checkout como invitado**
   - Obtención dinámica del nombre y precio del producto
   - Completar formulario de checkout
   - Selección de país y región desde selects
   - Confirmación de la orden
   - Captura de evidencia (screenshot)

Estos flujos permiten validar navegación, formularios, selects dinámicos, botones y confirmaciones, cubriendo gran parte del comportamiento del usuario.

---

## Calidad y estructura del código

El proyecto está organizado siguiendo **POM**, separando responsabilidades:

- `tests/`: definición de los casos de prueba
- `pages/`: lógica y acciones de cada página, tambien se encuentran los localizadores
- `conftest.py`: configuración del driver y fixtures. Se evita hardcodear la url y maneja la opcion por falta de certificado SSL faltante
- `base_page.py`: acciones reutilizables (esperas, input, clicks, lectura de texto)

---

## Próximas etapas

Como siguiente paso, se contempla la incorporación de **Gherkin con Cucumber (pytest-bdd)** para definir los escenarios de prueba en un lenguaje más legible y orientado al negocio, facilitando la escalabilidad del proyecto y la colaboración entre perfiles técnicos y no técnicos.

Adicionalmente, se evaluará la incorporación de mejoras como separación de datos de prueba, reportes automatizados y ejecución en pipelines de integración continua (CI/CD).

---

## Ejecución del proyecto

```bash
pip install -r requirements.txt
pytest -v

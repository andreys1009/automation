import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    """Добавление параметра командной строки для задания языка интерфейса."""
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Выберите язык интерфейса (например, 'en', 'ru', 'fr')"
    )


@pytest.fixture(scope="function")
def browser(request):
    """Фикстура для инициализации и закрытия браузера."""
    print("\nЗапуск браузера для теста...")

    # Получение языка из параметров командной строки
    user_language = request.config.getoption("language")

    # Настройка параметров Chrome
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # Инициализация WebDriver с ChromeDriverManager
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    yield driver

    print("\nЗакрытие браузера...")
    driver.quit()
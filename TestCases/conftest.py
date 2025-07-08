import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    return driver

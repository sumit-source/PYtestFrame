from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testlogin:
    def test_001 (self):
        import time
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support import expected_conditions
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
            # from selenium.common.exceptions import
        driver.get("https://app.hrone.cloud/login")
            # time.sleep(3)
            # driver.find_element(By.XPATH, "//input[@id='hrone-username']").click()
        WebDriverWait(driver,3).until(expected_conditions.element_to_be_clickable((By.XPATH,"//input[@id='hrone-username']")))
        driver.find_element(By.XPATH, "//input[@id='hrone-username']").send_keys("sumit.dubey@easyrewardz.com")
        driver.find_element(By.XPATH, "//button[@class = 'loginform btn btn-success btn-h-40 ladda-button']").click()
        WebDriverWait(driver,3).until(expected_conditions.element_to_be_clickable((By.XPATH,"//input[@id = 'hrone-password']")))
        driver.find_element(By.XPATH, "//input[@id = 'hrone-password']").send_keys("Shreeram@12345")
        WebDriverWait(driver,3).until(expected_conditions.element_to_be_clickable((By.XPATH,"//span[normalize-space()='LOG IN']")))
        driver.find_element(By.XPATH, "//span[normalize-space()='LOG IN']").click()
        time.sleep(5)
        try:
            image = driver.find_element(By.XPATH, "//img[contains(@src, 'smiley/good.png')]")
            time.sleep(3)
            assert image.is_displayed()
            print("Login successful: Smiley image found.")
        except:
            print("Login failed: Smiley image not found.")
            assert False
        WebDriverWait(driver,3).until(expected_conditions.element_to_be_clickable((By.XPATH,"//img[contains(@src, 'smiley/good.png')]")))
        driver.find_element(By.XPATH,"//img[contains(@src, 'smiley/good.png')]").click()
        driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        driver.quit()

    def test_002 (self):
        print("Running test_002")
        import time
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
            # from selenium.common.exceptions import
        driver.get("https://app.hrone.cloud/login")
            # time.sleep(3)
            # driver.find_element(By.XPATH, "//input[@id='hrone-username']").click()
        WebDriverWait(driver,3).until(expected_conditions.element_to_be_clickable((By.XPATH,"//input[@id='hrone-username']")))
        driver.find_element(By.XPATH, "//input[@id='hrone-username']").send_keys("sumit.dubey@easyrewardz.com")
        driver.find_element(By.XPATH, "//button[@class = 'loginform btn btn-success btn-h-40 ladda-button']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id = 'hrone-password']").send_keys("Test@123")
        time.sleep(5)
        driver.find_element(By.XPATH, "//span[normalize-space()='LOG IN']").click()
        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//div[@class='mat-mdc-snack-bar-label mdc-snackbar__label']")))
        if 'Invalid user credentials' in driver.find_element(By.XPATH, "//div[@class='mat-mdc-snack-bar-label mdc-snackbar__label']").text:
            assert True
        else:
            assert False
        driver.quit()

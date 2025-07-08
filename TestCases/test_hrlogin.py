import time
import pytest
from selenium.webdriver.common.by import By
class TestHRLogin:
    def testlogin_001(self,setup):
        self.driver = setup
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active']").click()
        self.driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(8)
        if "Dashboard" in self.driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text:
                print("Dashboard text found")
                assert True
        else:
                print("Dashboard text not found")
                assert False

    def testlogin_002(self,setup):
        self.driver = setup
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active']").click()
        self.driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active']").send_keys("Admin1")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(4)
        if "Invalid credentials" in self.driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text:
            assert True
        else:
            assert False

    def testlogin_003(self,setup):
        self.driver = setup
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active']").click()
        self.driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin1234")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(4)
        if "Invalid credentials" in self.driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text:
            assert True
        else:
            assert False
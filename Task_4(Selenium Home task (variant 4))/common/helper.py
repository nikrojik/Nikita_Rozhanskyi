from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
import time

delay_to_load_page = 10  # seconds

login_username = 'Admin'
login_password = 'admin123'

shift_name = 'RandomShiftName'

class TimeShifterTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    def login_page(self):
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//input[@name="username"]'))).send_keys(login_username)
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(login_password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def main_page(self):
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//span[text()="Admin"]'))).click()

        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//span[contains(text(),"Job")]'))).click()
        self.driver.find_element(By.XPATH, '//a[contains(text(),"Work Shifts")]').click()

        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//button[contains(.,"Add")]'))).click()

    def time_shift_page(self):
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//input[not(@placeholder)]'))).send_keys(shift_name)

        time.sleep(1)
        first_expander, second_expander = \
            self.driver.find_elements(By.XPATH, '//i[@class="oxd-icon bi-clock oxd-time-input--clock"]')

        first_expander.click()
        xpath_button_from = '//i[@class="oxd-icon bi-chevron-down oxd-icon-button__icon oxd-time-hour-input-down"]'
        button_from = self.driver.find_element(By.XPATH, xpath_button_from)
        button_from.click()
        button_from.click()
        button_from.click()

        second_expander.click()
        xpath_button_to = '//i[@class="oxd-icon bi-chevron-up oxd-icon-button__icon oxd-time-hour-input-up"]'
        self.driver.find_element(By.XPATH, xpath_button_to).click()

        self.driver.find_element(By.XPATH, '//input[contains(@placeholder,"Type for hints")]').send_keys('Odis')
        time.sleep(3)
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//div[@class="oxd-autocomplete-dropdown --positon-bottom"]'))).click()

        self.driver.find_element(By.XPATH, '//button[contains(.,"Save")]').click()

    def check_new_row(self):
        xpath_found_row = f'//div[@class="oxd-table-row oxd-table-row--with-border" and contains(., "{shift_name}")]'
        found_row = WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, xpath_found_row)))

        found_row.find_element(By.XPATH, f'//div[contains(., "{shift_name}")]')
        found_row.find_element(By.XPATH, '//div[contains(., "06:00")]')
        found_row.find_element(By.XPATH, '//div[contains(., "18:00")]')
        found_row.find_element(By.XPATH, '//div[contains(., "12.00")]')

    def remove_row_and_check(self):
        xpath_delete = f'//div[@class="oxd-table-row oxd-table-row--with-border" and contains(., "{shift_name}")]//i[@class="oxd-icon bi-trash"]'
        found_row = self.driver.find_element(By.XPATH, xpath_delete)
        found_row.find_element(By.XPATH, '//i[@class="oxd-icon bi-trash"]').click()
        self.driver.find_element(By.XPATH, '//button[contains(.,"Yes, Delete")]').click()
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, xpath_delete)
            assert 'Element not removed'
        except NoSuchElementException:
            pass

        self.driver.close()

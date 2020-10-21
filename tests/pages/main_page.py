from selenium.webdriver.common.by import By


class MainPage:
    URL = "http://127.0.0.1:5000/"
    BUTTON_UPLOAD = (By.XPATH, '/html/body/div/div/form/div/div[1]/button')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def test_button(self):
        up_button = self.browser.find_element(*self.BUTTON_UPLOAD)
        up_button.click()

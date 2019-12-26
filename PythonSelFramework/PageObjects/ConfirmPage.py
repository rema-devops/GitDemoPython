from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    confirmCheckout = (By.XPATH, "//button[@class='btn btn-success']")
    country = (By.ID, "country")
    country_link = (By.LINK_TEXT, 'India')
    terms_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "input[type=submit]")
    confirm_msg = (By.CSS_SELECTOR, "[class*='alert-success']")

    def getConfirmCheckout(self):
        return self.driver.find_element(*ConfirmPage.confirmCheckout)

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getCountryLink(self):
        return self.driver.find_element(*ConfirmPage.country_link)

    def confirmTermsCheckbox(self):
        return self.driver.find_element(*ConfirmPage.terms_checkbox)

    def confirmPurchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def confirmMessage(self):
        return self.driver.find_element(*ConfirmPage.confirm_msg).text

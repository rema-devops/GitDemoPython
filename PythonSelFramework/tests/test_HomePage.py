import time

from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self):
        homePage = HomePage(self.driver)
        homePage.getName().send_keys("Rema")
        homePage.getEmail().send_keys("xyz@gmail.com")
        homePage.getPassword().send_keys("abc@234")
        homePage.getCheckbox().click()
        self.selectOptionByText(homePage.getGender(), "Male")
        homePage.getDOB().send_keys("22-08-2010")
        time.sleep(4)
        homePage.getSubmit().click()
        alert =  homePage.getAlertMessage().text
        print(alert)
        assert ("Success" in alert)
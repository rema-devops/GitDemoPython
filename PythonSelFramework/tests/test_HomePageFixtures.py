import time

import pytest
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePageFixtures(BaseClass):

    def test_formSubmissionFixture(self, getData):
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData[0])
        homePage.getEmail().send_keys(getData[1])
        homePage.getPassword().send_keys(getData[2])
        homePage.getCheckbox().click()
        self.selectOptionByText(homePage.getGender(), getData[3])
        homePage.getDOB().send_keys(getData[4])
        time.sleep(4)
        homePage.getSubmit().click()
        alert =  homePage.getAlertMessage().text
        print(alert)
        assert ("Success" in alert)
        self.driver.refresh()

    @pytest.fixture(params=[("Randher", "xyz@gmail.com", "xyz@234", "Male", "22-08-2010"), ("Ritika", "abc@gmail.com", "abc@234", "Female", "26-08-2013")])
    def getData(self, request):
        return request.param


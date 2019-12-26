import time

import pytest
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePageFixturesDictionary(BaseClass):

    def test_formSubmissionFixtureDictionary(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        log.info("email is " + getData["email"])
        homePage.getEmail().send_keys(getData["email"])
        log.info("password is " + getData["password"])
        homePage.getPassword().send_keys(getData["password"])
        homePage.getCheckbox().click()
        log.info("gender is " + getData["gender"])
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        homePage.getDOB().send_keys(getData["dob"])
        time.sleep(4)
        homePage.getSubmit().click()
        alert =  homePage.getAlertMessage().text
        print(alert)
        assert ("Success" in alert)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param


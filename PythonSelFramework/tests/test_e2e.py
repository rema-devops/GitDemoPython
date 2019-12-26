import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = CheckoutPage(self.driver)
        confirmPage = ConfirmPage(self.driver)
        homePage.shopItems().click()
        cards=checkoutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == 'Blackberry':
                checkoutPage.getCardFooter()[i].click()
        #time.sleep(2)
        #self.driver.execute_script("scroll(0, -250);")
        checkoutPage.getCheckout().click()
        confirmPage.getConfirmCheckout().click()
        confirmPage.getCountry().send_keys('Ind')
        log.info("Entering country name as Ind")
        self.verifyLinkPresence('India')
        confirmPage.getCountryLink().click()
        time.sleep(5)
        confirmPage.confirmTermsCheckbox().click()
        confirmPage.confirmPurchase().click()
        log.info("Text received from application is:  "+confirmPage.confirmMessage())
        assert "Success! Thank you! ngksskour order will be delivered" in confirmPage.confirmMessage()

        self.driver.get_screenshot_as_file("screen.png")

import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self, text_to_verify):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text_to_verify)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getLogger(self):
            loggerName = inspect.stack()[1][3]
            logger = logging.getLogger(__name__)
            fileHandler = logging.FileHandler('logfile1.log')
            formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
            fileHandler.setFormatter(formatter)

            logger.addHandler(fileHandler)  # filehandler object
            logger.setLevel(logging.DEBUG)
            return logger

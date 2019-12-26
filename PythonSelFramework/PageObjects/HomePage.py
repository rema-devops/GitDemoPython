from selenium import webdriver

from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.CSS_SELECTOR, "[name='email']")
    pwd = (By.ID, "exampleInputPassword1")
    chkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    dob = (By.NAME, "bday")
    submit = (By.CSS_SELECTOR, "input[class='btn btn-success']")
    alertmsg = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.pwd)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.chkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getDOB(self):
        return self.driver.find_element(*HomePage.dob)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getAlertMessage(self):
        return self.driver.find_element(*HomePage.alertmsg)

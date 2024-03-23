import time
from typing import Any

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from PageObject.Add_Emp import AddEmployee
from PageObject.LoginPage import Login
from PageObject.employeeSearch import Employeesearch
from utilities.readproperties import Readconfig
from utilities.Logger import loggenrator



class Test_EMP_Search:
    url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    Log = loggenrator.Logen()

    def test_EMP_Search005(self,setup):
        self.driver = setup
        self.Log.info("opening Browser")
        self.driver.get(self.url)
        self.LP = Login(self.driver)
        self.LP.Enter_username(self.username)
        self.Log.info("Entering Username-->" + self.username)
        self.LP.Enter_password(self.password)
        self.Log.info("Entering Password-->" + self.password)
        self.LP.click_on_Login_Button()
        self.Log.info("click on Login Button")
        self.AE = AddEmployee(self.driver)
        self.AE.Click_pim()
        self.Log.info("click on Pim Button ")
        self.SE= Employeesearch(self.driver)
        self.SE.Enter_EMPName("Admin1")
        self.Log.info("Entering EMPName")
        time.sleep(4)
        self.SE.Search_Button()
        self.Log.info("Click On Search Button")
        self.Log.info("Search Found")
        time.sleep(4)
        if self.SE.search_Result()==True:
            self.LP.Click_On_menu_Button()
            self.driver.save_screenshot("C:\\OrangeHRm\\Screenshot\\orangeHRM.png")
            self.Log.info("click On Menu Button")
            self.LP.click_on_Logout_button()
            self.Log.info("click On Logout Button")
            self.Log.info("Search Found")
            self.Log.info("Test case 005 is passed")
            assert True

        else:
            self.LP.Click_On_menu_Button()
            self.driver.save_screenshot("C:\\OrangeHRm\\Screenshot\\orangeHRM.png")
            self.Log.info("click On Menu Button")
            self.LP.click_on_Logout_button()
            self.Log.info("click On Logout Button")
            self.driver.save_screenshot("C:\\OrangeHRm\\Screenshot\\OrangeHRM.png")
            self.Log.info("Test case005 is Failed")
            assert False


        self.Log.info("Test case005 is completed")












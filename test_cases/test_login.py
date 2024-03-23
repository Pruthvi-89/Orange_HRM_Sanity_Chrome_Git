import time

import pytest
from selenium import webdriver
import unittest
from PageObject.LoginPage import Login
from utilities.readproperties import Readconfig
from utilities.Logger import loggenrator



class Test_Login:
    url=Readconfig.geturl()
    username=Readconfig.getusername()
    password=Readconfig.getpassword()
    Log=loggenrator.Logen()


    def test_Login001(self,setup):
        self.driver=setup
        self.Log.info("Test case 001 is started is started")
        self.Log.info("opening browser")
        time.sleep(4)
        self.driver.get(self.url)
        time.sleep(4)
        self.Log.info("Going to url--> "+self.url)
        if self.driver.title=="OrangeHRM":
            assert True
            self.driver.save_screenshot("C:\\OrangeHRm\\Screenshot\\OrangeHRM.png")
            self.Log.info("Test case 001 is passed")
            self.Log.info("Page Tile-->"+self.driver.title)

        else:
            self.driver.save_screenshot("C:\\OrangeHRm\\Screenshot\\OrangeHRM.png")
            self.Log.info("Test case 001 is failed")
            assert False
        self.driver.close()
        self.Log.info("Test case 001 is Completed")


        self.Log.info("Test case is completed")
        # self.Log.debug("Debug")
        # self.Log.info("info")
        # self.Log.warning("warning")
        # self.Log.error("errro")
        # self.Log.critical("crictical")

    @pytest.mark.sanity
    def test_login02(self,setup):
        self.driver=setup
        self.Log.info("Test case 002 is started")
        self.Log.info("opening Browser")
        self.driver.get(self.url)
        self.Log.info("Going To url-->"+self.url)
        self.LP= Login(self.driver)
        self.LP.Enter_username(self.username)
        self.Log.info("Entering Username-->"+self.username)
        self.LP.Enter_password(self.password)
        self.Log.info("Entering Password-->"+self.password)
        self.LP.click_on_Login_Button()
        self.Log.info("Click on Login Button")



        if self.LP.validate_Login()==True:
            self.LP.Click_On_menu_Button()
            self.driver.save_screenshot("C:\\OrangeHRm\\Screenshot\\orangeHRM.png")
            self.Log.info("click On Menu Button")
            self.LP.click_on_Logout_button()
            self.Log.info("click On Logout Button")
            self.Log.info("Test case002 is passed")
            assert True

        else:
            self.Log.info("Test case002 is failed")
            self.driver.save_screenshot("C:\\OrangeHRm\\Screenshot\\OrangeHRM.png")
            assert False

        self.driver.close()
        self.Log.info("Test case002 is Completed")







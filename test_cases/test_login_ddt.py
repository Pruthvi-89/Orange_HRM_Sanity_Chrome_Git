import time

from selenium import webdriver
import unittest
from PageObject.LoginPage import Login
from utilities import xlutils
from utilities.readproperties import Readconfig
from utilities.Logger import loggenrator


class Test_Login_ddt:
    url = Readconfig.geturl()
    # username=Readconfig.getusername()
    # password=Readconfig.getpassword()
    Log = loggenrator.Logen()
    path = "C:\\OrangeHRm\\test_cases\\TestData\\LoginData.xlsx"


    def test_login02(self, setup):
        global r
        self.driver = setup
        self.Log.info("Test case 002 is started")
        self.Log.info("opening Browser")
        self.driver.get(self.url)
        self.Log.info("Going To url-->" + self.url)
        self.LP = Login(self.driver)
        self.Rows = xlutils.getrowcount(self.path, "Sheet1")
        print("No of Rows -->", self.Rows)

        Login_Status = []
        for r in range(2, self.Rows+1):
            self.username = xlutils.readdata(self.path, 'Sheet1', r, 2)
            self.password = xlutils.readdata(self.path, 'Sheet1', r, 3)
            self.LP.Enter_username(self.username)
            self.Log.info("Entering Username-->")
            self.LP.Enter_password(self.password)
            self.Log.info("Entering Password-->")
            self.LP.click_on_Login_Button()
            self.Log.info("Click on Login Button")

            if self.LP.validate_Login() == True:
                self.LP.Click_On_menu_Button()
                self.driver.save_screenshot("C:\OrangeHRm\Screenshot\\"+self.username+self.password+"test_login006--Pass.png ")
                self.Log.info("click On Menu Button")
                self.LP.click_on_Logout_button()
                self.Log.info("click On Logout Button")
                Login_Status.append("Pass")
                time.sleep(2)
                self.Rows = xlutils.writedata(self.path, "Sheet1", r, 4,"Pass")


            else:
                Login_Status.append("Fail")
                time.sleep(4)
                self.Rows = xlutils.writedata(self.path, "Sheet1", r, 4, "Fail")
                self.driver.save_screenshot("C:\OrangeHRm\Screenshot\\"+self.username+self.password+"test_login006--Fail.png ")

        time.sleep(4)
        print(Login_Status)
        if self.LP.Capture_Invalid_massage()==True:
            self.Log.info("Test Login006 is passed")
            self.driver.close()
            assert True

        else:
            self.Log.info("Test Login006 is Failed")
            self.driver.close()
            assert False

        self.Log.info("Test Login006 is Completed")
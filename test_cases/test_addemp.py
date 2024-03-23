import time

import pytest

from PageObject.Add_Emp import AddEmployee
from PageObject.LoginPage import Login
from utilities.readproperties import Readconfig
from utilities.Logger import loggenrator


class Test_add_employee:
    url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    Log = loggenrator.Logen()

    @pytest.mark.sanity
    def test_add_employee(self, setup):
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
        self.AE.Click_add()
        self.Log.info("click on add employee")
        self.AE.Enter_FirstName("Pruthviraj")
        self.Log.info("Entering FirstName")
        self.AE.Enter_MiddleName("Ramesh")
        self.Log.info("Entering MiddleName")
        self.AE.Enter_LastName("Deokate")
        self.Log.info("Entering Lastname")
        time.sleep(2)
        self.AE.click_on_SaveButton()
        self.Log.info("click on save Button")

        time.sleep(4)
        if self.AE.Add_Employee_Status() == True:
            self.driver.save_screenshot("C:\\OrangeHRm\\Screenshot\\OrangHrm.png")
            self.Log.info("Test case 003 is failed")
            assert True

        else:
            self.driver.save_screenshot("C:\\OrangeHRm\\Screenshot\\OrangHrm.png")
            self.Log.info("Test case 003 is passed")
            assert False

        self.driver.close()

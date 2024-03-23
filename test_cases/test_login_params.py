from PageObject.LoginPage import Login
from utilities.Logger import loggenrator
from utilities.readproperties import Readconfig


class Test_login_params:
    url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    Log = loggenrator.Logen()

    def test_login_params004(self, setup, getdataforlogin):
        self.driver = setup
        self.Log.info("Test case 004 is started")
        self.Log.info("opening Browser")
        self.driver.get(self.url)
        self.Log.info("Going To url-->" + self.url)
        self.LP = Login(self.driver)
        self.LP.Enter_username(getdataforlogin[0])
        self.Log.info("Entering Username-->" + getdataforlogin[0])
        self.LP.Enter_password(getdataforlogin[1])
        self.Log.info("Entering Password-->" + getdataforlogin[1])
        self.LP.click_on_Login_Button()
        self.Log.info("Click on Login Button")

        if self.LP.validate_Login():
            if getdataforlogin[2] == "pass":
                self.LP.Click_On_menu_Button()
                self.driver.save_screenshot("C:\\OrangeHRm\\Screenshot\\orangeHRM.png")
                self.Log.info("click On Menu Button")
                self.LP.click_on_Logout_button()
                self.Log.info("click On Logout Button")
                self.Log.info("Test case004 is passed")
                assert Truec
            else:
                self.Log.info("Test case004 is failed")
                self.driver.save_screenshot("C:\\OrangeHRm\\Screenshot\\OrangeHRM.png")
                assert False
        else:
            if getdataforlogin[2] == "Fail":
                assert True
            else:
                self.Log.info("Test case004 is failed")
                self.driver.save_screenshot("C:\\OrangeHRm\\Screenshot\\OrangeHRM.png")
                assert False
        self.driver.close()
        self.Log.info("Test case004 is Completed")

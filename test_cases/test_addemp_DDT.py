import time

import pytest

from PageObject.Add_Emp import AddEmployee
from PageObject.LoginPage import Login
from utilities import xlutils
from utilities.readproperties import Readconfig
from utilities.Logger import loggenrator


class Test_add_employee_DDT:
    url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    Log = loggenrator.Logen()
    path="C:\\OrangeHRm\\test_cases\\TestData\\EmployeeList.xlsx"

    @pytest.mark.sanity
    def test_add_employee_DDT_005(self, setup):
        global r
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
        self.rows = xlutils.getrowcount(self.path,'Sheet1')
        print("Number of Rows--->")
        self.AE.Click_pim()
        self.Log.info("click on Pim Button ")
        self.AE.Click_add()

        Status_List=[]
        for r in range (2,self.rows+1):
            self.FirstName = xlutils.readdata(self.path, 'Sheet1', r, 2)
            self.MiddleName = xlutils.readdata(self.path, 'Sheet1', r, 3)
            self.LastName = xlutils.readdata(self.path, 'Sheet1', r, 4)
            self.AE.Enter_FirstName(self.FirstName)
            self.Log.info("Entering FirstName--->")
            self.AE.Enter_MiddleName(self.MiddleName)
            self.Log.info("Entering MiddleName-->")
            self.AE.Enter_LastName(self.LastName)
            self.Log.info("Entering Lastname-->")
            time.sleep(4)
            self.AE.click_on_SaveButton()
            self.Log.info("click on save Button")

            time.sleep(4)
            if   self.AE.Add_Employee_Status() == True:
                 self.AE.Add_employee()
                 time.sleep(4)
                 Status_List.append("Pass")
                 xlutils.writedata(self.path,"Sheet1", r, 5, "Pass")
                 self.driver.save_screenshot("C:\\OrangeHRm\\Screenshot\\OrangHrm.png")

            else:
                  Status_List.append("Fail")
                  xlutils.writedata(self.path,"Sheet1",r,5,"Fail")
                  self.driver.save_screenshot("C:\\OrangeHRm\\Screenshot\\OrangHrm.png")

        print(Status_List)


        self.LP.Click_On_menu_Button()
        self.Log.info("click On Menu Button")
        self.LP.click_on_Logout_button()
        self.Log.info("click On Logout Button")
        self.Log.info("Test case005 is passed")

        if "Fail"  not in Status_List:
            self.Log.info("Test case 005 is passed")
            assert True
        else:
            self.Log.info("Test case 005 is Fail")
            assert False

        self.Log.info("Test case005 is Completed")
        self.driver.close()



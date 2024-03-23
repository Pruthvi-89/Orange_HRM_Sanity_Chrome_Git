import time

import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common import NoSuchElementException as EC




class AddEmployee:
       Click_On_Pim_Xpath=(By.XPATH,"//span[normalize-space()='PIM']")
       Click_On_Add_Button_Xpath=(By.XPATH,"//button[normalize-space()='Add']")
       Text_Enter_FirstName_Xpath=(By.XPATH,"//input[@placeholder='First Name']")
       Text_Enter_MiddleName_Xpath=(By.XPATH,"//input[@placeholder='Middle Name']")
       Text_Enter_LastName_Xpath=(By.XPATH,"//input[@placeholder='Last Name']")
       Click_On_Save_Button_XPATH=(By.XPATH,"//button[@type='submit']")
       Personal_Deatils_TAB_XPATH=(By.XPATH,"//h6[normalize-space()='Personal Details']")
       Click_On_Add_EMP_XPATH=(By.XPATH,"//a[normalize-space()='Add Employee']")

       def __init__(self,driver):
           self.driver = driver


       def Click_pim(self):
           self.driver.find_element(*AddEmployee.Click_On_Pim_Xpath).click()


       def Click_add(self):
           self.driver.find_element(*AddEmployee.Click_On_Add_Button_Xpath).click()


       def Enter_FirstName(self,FirstName):
           self.driver.find_element(*AddEmployee.Text_Enter_FirstName_Xpath).send_keys(FirstName)


       def Enter_MiddleName(self,MiddleName):
           self.driver.find_element(*AddEmployee.Text_Enter_MiddleName_Xpath).send_keys(MiddleName)


       def Enter_LastName(self,LastName):
           self.driver.find_element(*AddEmployee.Text_Enter_LastName_Xpath).send_keys(LastName)


       def click_on_SaveButton(self):
           self.driver.find_element(*AddEmployee.Click_On_Save_Button_XPATH).click()


       def Add_employee(self):
           self.driver.find_element(*AddEmployee.Click_On_Add_EMP_XPATH).click()



       def Add_Employee_Status(self):
           try:
               self.driver.implicitly_wait(5)
               self.driver.find_element(*AddEmployee.Personal_Deatils_TAB_XPATH)
               return True


           except EC :
               return False










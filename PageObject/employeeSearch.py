from selenium.webdriver.common.by import By


class Employeesearch:


    Text_EmpName_XPATH=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")
    Text_Search_EMP_XPATH=(By.XPATH,"//button[@type='submit']")
    Search_Result_CSS=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")

    def __init__(self, driver):
        self.driver = driver


    def Enter_EMPName(self,EMPName):
        self.driver.find_element(*Employeesearch.Text_EmpName_XPATH).send_keys(EMPName)


    def Search_Button(self):
        self.driver.find_element(*Employeesearch.Text_Search_EMP_XPATH).click()


    def search_Result(self):
        search = self.driver.find_elements(*Employeesearch.Search_Result_CSS)
        search_len=len(search)
        if search == 0:
            return False

        elif search_len == 0:
            self.driver.find_element(*Employeesearch.Search_Result_CSS).text
            retrun = True


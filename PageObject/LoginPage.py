
from selenium.webdriver.common.by import By


class Login:

    Enter_username_XPATH=(By.XPATH,"//input[@placeholder='Username']")
    Enter_Password_XPATH=(By.XPATH,"//input[@placeholder='Password']")
    Click_On_Login_Button_XPATH = (By.XPATH, "//button[@type='submit']")
    CAPTURE_INVALID_MASSAGE_XPATH=(By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
    Click_On_menu_Button_XPATH=(By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
    Click_On_Logout_Button_XPATH=(By.XPATH,"//a[normalize-space()='Logout']")





    def __init__(self,driver):
        self.driver=driver

    def Enter_username(self,username):
        self.driver.find_element(*Login.Enter_username_XPATH).send_keys(username)

    def Enter_password(self,password):
        self.driver.find_element(*Login.Enter_Password_XPATH).send_keys(password)


    def Capture_Invalid_massage(self):
        try:
            self.driver.find_element(*Login.CAPTURE_INVALID_MASSAGE_XPATH)
            return True

        except:
            return False




    def click_on_Login_Button(self):
        self.driver.find_element(*Login.Click_On_Login_Button_XPATH).click()


    def Click_On_menu_Button(self):
        self.driver.find_element(*Login.Click_On_menu_Button_XPATH).click()




    def click_on_Logout_button(self):
        self.driver.find_element(*Login.Click_On_Logout_Button_XPATH).click()



    def validate_Login(self):
        try:
            self.driver.find_element(*Login.Click_On_menu_Button_XPATH)
            return True

        except:
            return False






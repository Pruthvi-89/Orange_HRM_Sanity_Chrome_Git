import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

# from selenium.webdriver.chrome import webdriver

# Chrome_options = webdriver.ChromeOptions()
# Chrome_options.add_argument("headless")
#
#
# def pytest_metadata(metadata):
#     metadata["Environment"] = "Test"
#     metadata["Project Name"] = "OrangeHRM"
#     metadata["module Name"] = "Employee"
#     metadata["Tester"] = "Pruthviraj"
#     metadata.pop("package", None)
#     metadata.pop("Plugins", None)
#     metadata.pop("platform", None)
#
#
# @pytest.fixture(params=[
#     ("Admin", "admin123"),
#     ("Admin1", "admin123"),
#     ("Admin", "admin1231"),
#     ("Admin1", "admin1231")
# ])
# def getdataforlogin(request):
#     return request.param
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
#
# @pytest.fixture()
# def setup(browser):
#     if browser == 'chrome':
#         print("Launching Chrome Browser")
#         browser = webdriver.Chrome()
#     elif browser == 'firefox':
#         print("Launching Firefox Browser")
#         browser = webdriver.Firefox()
#     elif browser == 'edge':
#         print("Launching Edge Browser")
#         browser = webdriver.Edge()
#     # if browser == 'headless':
#     else:
#         print("headless mode")
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument("headless")
#         browser = webdriver.Chrome(options= chrome_options)
#         browser = webdriver.Chrome()


# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     #driver = webdriver.Chrome(options=Chrome_options)
#     driver.implicitly_wait(5)
#     # driver.get("https://opensource-demo.orangehrmlive.com/")
#     driver.maximize_window()
#     return driver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    #driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    return driver

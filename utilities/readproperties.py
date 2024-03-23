import configparser

config = configparser.RawConfigParser()

config.read("C:\\OrangeHRm\\PageObject\\configuration\\config.ini")


class Readconfig():

    @staticmethod
    def geturl():
        url = config.get("common info","url")
        return url

    @staticmethod
    def getusername():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def getpassword():
        password = config.get("common info", "password")
        return password

    @staticmethod
    def getfirstname():
        firstname = config.get("common info", "firstname")
        return firstname

    @staticmethod
    def getmiddlename():
        middlename = config.get("common info", "middlename")
        return middlename

    @staticmethod
    def getlastname():
        lastname = config.get("common info", "lastname")
        return lastname

    @staticmethod
    def getEMPName():
        EMPNAME= config.get("common info","EMPNAME")
        return EMPNAME

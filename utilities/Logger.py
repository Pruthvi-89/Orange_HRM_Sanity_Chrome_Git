import inspect
import logging

class loggenrator:

    @staticmethod
    def Logen():

        name = inspect.stack()[1][3]
        logger=logging.getLogger(name)
        logfile=logging.FileHandler("C:\\OrangeHRm\\Log\\OrangeHRM_Automaton.log")
        format=logging.Formatter("%(asctime)s: %(levelname)s : %(name)s : %(funcName)s %(lineno)s : %(message)s")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger

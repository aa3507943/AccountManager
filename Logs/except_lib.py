import logging
import os

class ExceptionHandler:
    def __init__(self, msg: str, exceptionLevel: str):
        self.msg = msg
        self.exceptionLevel = exceptionLevel
        self.FORMAT = '\n%(asctime)s %(levelname)s: %(message)s'
        self.DATE_FORMAT = '%Y%m%d %H:%M:%S'
        self.level_recognizer()
        logging.basicConfig(level=self.level, format=self.FORMAT, datefmt= self.DATE_FORMAT, filemode="a+", encoding= "utf-8", filename= os.path.abspath("Logs/Exception.log"))
        self.record_logs()
        print(msg)
        
    def level_recognizer(self):
        if self.exceptionLevel.lower() == "debug":
            self.level = logging.DEBUG
        elif self.exceptionLevel.lower() == "info":
            self.level = logging.INFO
        elif self.exceptionLevel.lower() == "warning":
            self.level = logging.WARNING
        elif self.exceptionLevel.lower() == "error":
            self.level = logging.ERROR
        elif self.exceptionLevel.lower() == "critical":
            self.level = logging.CRITICAL
            
    def record_logs(self):
        if self.exceptionLevel.lower() == "debug":
            logging.debug(self.msg, exc_info= True)
        elif self.exceptionLevel.lower() == "info":
            logging.info(self.msg, exc_info= True)
        elif self.exceptionLevel.lower() == "warning":
            logging.warning(self.msg, exc_info= True)
        elif self.exceptionLevel.lower() == "error":
            logging.error(self.msg, exc_info= True)
        elif self.exceptionLevel.lower() == "critical":
            logging.critical(self.msg, exc_info= True)
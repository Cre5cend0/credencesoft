import logging
import os.path


def logger():
    log_item = logging.getLogger(__name__)

    # uncomment the below code if you do not want to clear logs for each test run
    if os.path.exists("./reports/logFile.log"): # clear log file when running main.py
        with open('./reports/LogFile.log', 'w+') as logFile:
            logFile.seek(0)
            logFile.truncate()

    # change the below file location in file handler if running on a different machine
    file_handler = logging.FileHandler("/Users/manishraj/Documents/pycharm_projects/credencesoft/reports/LogFile.log")
    log_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    file_handler.setFormatter(log_format)
    if not log_item.hasHandlers():
        log_item.addHandler(file_handler)
    log_item.setLevel(logging.INFO)
    return log_item


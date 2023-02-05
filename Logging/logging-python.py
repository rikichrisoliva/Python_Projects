import logging  # built in module in Python, no need to install

# level=logging.INFO means you're going to get INFO level and above
# filemode "w" means create the file every single time, overriding a file if that already exist. There are other modes.
logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")
# the command logging.basicConfig can only be run one-time
# asctime is a special property which is a human readable time. Other attributes can be found in https://docs.python.org/3/library/logging.html#logrecord-attributes.
# %()s where s means string.

# different levels of logging in this order. debug is the least important. info is 2nd ...
# by default, when you use the logging module, you're only going to get the output for anything that's at the warning level or above (error or critical)
# so when you run the commands below, you're only going to get the warning, error, critical
# the output in the console or in the logs (file) would show the level, the root logger, and the message which you have enclosed in ""
x = 2
logging.debug("debug message")
logging.info(f"info message. x value is {x}")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")

# log a stack trace - an exception occurred
# without exc_info=True as argument, the exception occurred would not be logged.
try:
    10 / 0
except ZeroDivisionError:
    logging.error("This is a message to be logged", exc_info=True)

# for custom function logging.exception, no need to pass the exc_info=True argument. Message type will be ERROR.
try:
    20 / 0
except ZeroDivisionError:
    logging.exception("This is a message to be logged")

# to create a custom logger
# inside () put the name of the logger that you want. If it doesn't exist, it would create for you.
# if you have multiple Python modules, no need to pass the logger object around, you can use the logging.getLogger("name") if the "name" already exists.
# the convention is to use __name__ variable as logger, and to have one logger for each Python module.
# why __name__ because that gives you the name of the current module which is unique in your Python project
logger = logging.getLogger(__name__)
# for this logger to go to a separate file, we need to setup something called "handler"
# there's all kinds of other handlers related to HTTP, email, etc.
handler = logging.FileHandler('test.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("test the custom logger")
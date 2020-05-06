import logging

#Log Levels: Debug,Info,Warning,Error,Critical

logging.basicConfig(filename = "logs/test.log",
					format='%(asctime)s: %(levelname)s: %(message)s',
					level=logging.DEBUG)            # Lowest level ensures all logs from lowest to highest

logging.debug("This is a debug message!")
logging.info("This is a info message!")
logging.warning("This is a warning message!")
logging.error("This is a error message!")
logging.critical("This is a critical message!")
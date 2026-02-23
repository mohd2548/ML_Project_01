# from src.mlproject import logger
# in more beter way we can write 
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys

if __name__=="__main__":
    logging.info("THE EXECUTION HAS STARTED!!!!!!!!")
    try:
        a=1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
        
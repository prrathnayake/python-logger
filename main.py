from src.logger import *

if __name__ == "__main__":
    logger = MyLogger.__call__().get_logger()
    logger.info("Hello, Logger")
    logger.debug("bug occured")
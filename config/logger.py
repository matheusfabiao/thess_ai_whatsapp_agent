import logging


class Logger:
    def __init__(self):
        self.__logger = logging.getLogger(__name__)
        self.__logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
        )
        handler.setFormatter(formatter)
        self.__logger.addHandler(handler)

    def get_logger(self):
        return self.__logger

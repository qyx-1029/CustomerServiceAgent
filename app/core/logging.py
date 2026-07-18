import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


LOG_DIR = Path("logs")


def setup_logging():

    # 创建日志目录
    LOG_DIR.mkdir(exist_ok=True)


    logger = logging.getLogger()

    logger.setLevel(logging.INFO)


    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )


    # 文件日志
    file_handler = RotatingFileHandler(
        filename=LOG_DIR / "app.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)


    # 控制台日志
    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)


    # 防止重复添加handler
    if not logger.handlers:

        logger.addHandler(file_handler)

        logger.addHandler(console_handler)
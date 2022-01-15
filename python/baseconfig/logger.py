# -*- coding:utf-8 -*-
"""
    日志配置
"""
import logging
import logging.handlers
import os

class Logger(object):
    """
    日志配置
    """

    def __init__(self, loggername):
        """ 创建一个logger """
        self.logger = logging.getLogger(loggername)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于将日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        # 指定文件输出路径，注意logs是个文件夹，一定要加上/，不然会导致输出路径错误，把logs变成文件名的一部分了
        info_log_path = os.path.abspath(os.path.dirname(
            os.path.dirname(__file__)))+"/logs/"
        info_logname = info_log_path + 'info.log'  # 指定输出的日志文件名
        # 指定utf-8格式编码，避免输出的日志文本乱码
        # info_fh = logging.FileHandler(info_logname, encoding='utf-8')
        info_fh = logging.handlers.RotatingFileHandler(
            info_logname, encoding = 'utf-8', mode = "w", maxBytes = 80 * 1204 * 1024, backupCount = 10)
        # info_fh = logging.handlers.TimedRotatingFileHandler(info_logname, when='D', interval=1, backupCount=20, encoding=None, delay=False, utc=False, atTime=None)
        info_fh.setLevel(logging.INFO)

        # 创建一个handler，用于写入日志文件
        # 指定文件输出路径，注意logs是个文件夹，一定要加上/，不然会导致输出路径错误，把logs变成文件名的一部分了
        err_log_path = os.path.abspath(os.path.dirname(
            os.path.dirname(__file__)))+"/logs/"
        err_log_name = err_log_path + 'error.log'  # 指定输出的日志文件名
        # 指定utf-8格式编码，避免输出的日志文本乱码
        err_fh = logging.FileHandler(err_log_name, encoding='utf-8')
        err_fh = logging.handlers.RotatingFileHandler(
             err_log_name, encoding = 'utf-8', mode = "w", maxBytes = 80 * 1024 * 1024, backupCount = 10000)
        err_fh.setLevel(logging.ERROR)

        # 定义handler的输出格式
        formatter = logging.Formatter(
            '%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        ch.setFormatter(formatter)
        info_fh.setFormatter(formatter)
        err_fh.setFormatter(formatter)
        # 给logger添加handler
        self.logger.addHandler(ch)
        self.logger.addHandler(info_fh)
        self.logger.addHandler(err_fh)

    def error(self, message):
        """ 定义一个函数，回调logger实例 """
        log = self.logger
        return log.error(message)

    def info(self, message):
        """定义一个函数，回调logger实例 """
        log = self.logger
        return log.info(message)

    def debug(self, message):
        """定义一个函数，回调logger实例 """
        log = self.logger
        return log.debug(message)

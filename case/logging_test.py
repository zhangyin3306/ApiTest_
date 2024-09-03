import logging
# from logging.handlers import RotatingFileHandler

#1、 创建一个 logger,设置日志级别
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)  # 设置 logger 的全局级别

# 创建 handler 输出到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # 控制台只显示 INFO 级别以上的日志
formatter = logging.Formatter('%(asctime)s %(name)s  %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# 创建 handler 输出到文件
file_handler=logging.FileHandler("../case/test.log",encoding='utf-8')
file_handler.setLevel(logging.INFO)  # 文件记录所有 DEBUG 级别以上的日志
file_formatter = logging.Formatter('%(asctime)s %(name)s  %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# 记录日志消息
logger.debug('this is rizhi ')
logger.info('这是一个 info 消息，将会记录到文件和控制台')
logger.warning('这是一个 warning 消息，将会记录到文件和控制台')
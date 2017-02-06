import os
import platform
import logging

if platform.platform().startswith('Window'):
  logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                              os.getenv('HOMEPATH'),
                              'test.log')
else:
  # 使用os.path.join
  # 而不是拼接字符串，原因是这个函数会确保路径复合当前操作系统的预期格式
  logging_file = os.path.join(os.getenv('HOME'),
                              'test.log')

print("Logging to", logging_file)

logging.basicConfig(
  level = logging.DEBUG,
  format = '%(asctime)s : %(levelname)s : %(message)s',
  filename = logging_file,
  filemode = 'w'
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")

import logging

print(dir(logging))


logging.basicConfig(filename="LogFile.txt",filemode='a',format="(%(asctime)s) => %(name)s | %(levelname)s | '%(message)s'",datefmt="%d-%B-%Y  %H:%M:%S")

logging.critical('Hi , This is critical error')

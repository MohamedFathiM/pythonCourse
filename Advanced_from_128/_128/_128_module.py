
# when run file directly ,__name__ = __main__
# print(__name__)

# will be run when import this file
print('Hello From _128_module')

def hello():
    print('Print Function from file one')

if True:
    print('true')
else:
    print('false')


if __name__ == "__main__" :
    print('Run File Directly')
else:
    print('You are not running this file directly')

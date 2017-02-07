def mydecorator(f):
  def swrap_f(*args, **kw):
    print(__name__)
    print('function will be called')
    return f(*args, **kw)
  return swrap_f

@mydecorator
def hello_decorator():
  print('be called')

hello_decorator()

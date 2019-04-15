def log(*text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('begin call')
            if isinstance(text,None):
                print('call %s(), %s' % (func.__name__))
            else:
                print('call %s(), %s' % (func.__name__, text))
            c=func(*args,**kw)
            print('end call')
            return c
        return wrapper
    return decorator


@log
def now():
    print('execute test')
now()

@log('execute test')
def test():
    print('test')
test()
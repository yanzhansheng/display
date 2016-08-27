import functools


def pre_print(func):
    @functools.wraps(func)
    def wraps(*args,**kwargs):
        print 'start'
        func(*args,**kwargs)
        print 'stop'
    return wraps
@pre_print
def print_zhong(*args,**kwargs):
    """my name is print_zhong"""
    for i in args:
        print i
    for key,value in kwargs.items():
        print key,value

print_zhong(1,2,3,name='laoyan',gender='man')
print print_zhong.__doc__
print print_zhong.__name__
print 'wo de shen a'


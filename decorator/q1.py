def dec(func):
    def wraper():
        return func+2
    return wraper
@dec
def asd():
    return 5+6

class MyError(Exception):
    def __init__(self,msg):
        self.msg=msg

    def __str__(self):
        return self.msg

try:
    raise MyError('My Error 1')
except MyError as e:
    print(e)
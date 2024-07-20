# class negativeAge(Exception):
#     def __init__(self,msg):
#         self.msg=msg
#
#     def __str__(self):
#         return self.msg

class negativeAge(Exception):
   pass


def stage(age):
    if age<0:
        raise negativeAge("Age should not be negative")

try:
  stage(-1)
except negativeAge as e:
    print(e)
except Exception as e:
    print(e)
class student:
 def __init__(self,roll,name,dept):
    self.roll=roll
    self.name=name
    self.dept=dept
 def display(self):
    print(f'Roll :{self.roll}\n Name :{self.name} dept :{self.dept}')
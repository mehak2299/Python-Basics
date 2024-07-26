# Pickle
# Storing Data

import student,pickle

studs=[student.student(10,'one','cs'),student.student(20,'two','mg')]

with open('students.data','wb')as f:
    for i in studs:
        pickle.dump(i,f)
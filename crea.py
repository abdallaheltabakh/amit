# class Student():
#     name = "abdallah";
#     age = 20;
#     gpa = 3.2;
#     gender="male" 
#     def student_info(self):
#         print(f"student name:{self.name}")
#         print(f"student age:{self.age}")
#         print(f"student gpa:{self.gpa}")
#         print(f"student gender:{self.gender}")
# # print(Student.name)
# # print(Student.age)
# # print(Student.gpa)
# # print(Student.gender)
# s=Student()
# s.student_info()
import numpy as np
# x=np.array(4)
y=np.array([1,2,3,4])
# print(x==y)

m=np.array([[1,8,8,5],
           [4,9,8,4]])
print(m.ndim)
print(m.shape)
m=m.reshape(4,2)
print(m[1,1])
print(y[-1])
print(y[2:])
# print()
# print()



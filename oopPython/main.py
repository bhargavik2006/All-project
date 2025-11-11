# class Student:
#     name="bhargavi"
# s1=Student()
# print(s1.name)
# s2=Student()
# print(s2.name)


# class Car:
#     color="blue"
#     brand="mercedes"
# car1=Car()
# print(car1.color)
# print(car1.brand)


# class Student:
#     collage="Presidency University" #class attribute
#     def __init__(self,fullname,marks):#parameterized constructor
#         self.name=fullname #object attribute
#         self.marks=marks
#         print("adding new student to the database")
# s1=Student("bhargavi",100)
# print(s1.name,s1.marks)
#
# s2=Student("amruta",99)
# print(s2.name,s2.marks)
# print(Student.collage)


# class Student:
#     collage="Presidency University" #class attribute
#     def __init__(self,fullname,marks):#parameterized constructor
#         self.name=fullname #object attribute
#         self.marks=marks
#     def welcome(self):
#         print("welcome student,", self.name)
#     def get_marks(self):
#         return self.marks
# s1=Student("bhargavi",100)
# print(s1.name,s1.marks)
# s1.welcome()
# print(s1.get_marks())
# s2=Student("amruta",99)
# print(s2.name,s2.marks)
# s2.welcome()
# print(s2.get_marks())

#
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     @staticmethod
#     def hello():
#         print("hiiiiiiiiiii")
#     def avg_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hi,", self.name,"your avg score is: ", sum/3)
#
# s1=Student("tony",[99,58,78])
# s1.avg_avg()
# s1.name="abcd"
# s1.avg_avg()
# s1.hello()

class Account:
    def __init__(self,balance,account):
        self.balance=balance
        self.account_no=account
    def debit(self,amount):
        self.balance-=amount
        print("Rs.", amount," was debited,you current balance is :",self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print("Rs.", amount," was debited,you current balance is :",self.get_balance())
    def get_balance(self):
        return self.balance




acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)


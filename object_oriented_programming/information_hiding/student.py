class Student:
    def __init__(self, name=None, rollNumber=None):
        self.__name = name
        self.__rollNumber = rollNumber

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber


quinn = Student("Quinn", 13501)
print(f"Student's name : {quinn.getName()} and roll number is {quinn.getRollNumber()}")
quinn.setName("Jessica")
print(quinn.getName())
quinn.setRollNumber(1234)
print(quinn.getRollNumber())

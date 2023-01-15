# bad example!!!
# class User:
#     def __init__(self, username=None, password=None):
#         self.username = username
#         self.password = password
#
#     def login(self, username, password):
#         if ((self.username.lower() == username.lower()) and (self.password == password)):
#             print("Access granted!")
#         else:
#             print("Invalid credentials!")
    # def setUsername(self, x):
    #     self.__username = x
    #
    # def getUsername(self):
    #     return self.__username


# good example!!!
class User:
    def __init__(self, userName=None, password=None):
        self.__userName = userName
        self.__password = password

    def login(self, userName, password):
        if ((self.__userName.lower()== userName.lower()) and (self.__password == password)):
            print("Access granted against username: ", self.__userName, "and password: ", self.__password)
        else:
            print("Invalid credentials!!!")


Steve = User("Steve", 1234)
print("Entering correct username and password: ")
Steve.login("steve", 1234)

print("Entering wrong username and password: ")
Steve.login("stevie", 4321)

print("Entering correct username and password: ")
Steve.login("steve", 1234)
# print("Before setting: ", Steve.getUsername())
# Steve.setUsername("Stevie the GMM staff")
# print("After setting: ", Steve.getUsername())
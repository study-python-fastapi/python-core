class User:
    def __init__(self,username,email,password):
        self.__username = username
        self.__email = email
        self.__password = password
    def info(self):
        print(self.__dict__)
    def set_info(self,attr,value):
        self.__dict__[attr]=value
        return {attr : self.__dict__[attr]}
User1 = User("Tom228","Tom228@gmail.com","TomTomqwertyqwerty")
User1.info()
print(User1.set_info("password","qwertyqwerty"))


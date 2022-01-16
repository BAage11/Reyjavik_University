# class that holds information about a certain user
class User:
    def __init__(self,id,name,password):
        self.__id = id
        self.__name = name
        self.__password = password
    # GET
    def getName(self):
        return self.__name
    def getId(self):
        return self.__id
    def getPassword(self):
        return self.__password
    # SET
    def setId(self,newId):
        self.__id = newId
    def setName(self,newName):
        self.__name = newName
    def setPassword(self, newPassword):
        self.__password = newPassword
    def __str__(self):
        return '{},{},{}'.format(str(self.getId()),self.getName(),self.getPassword())

# class that holds information about a certain order
class Order:
    def __init__(self,id,userId,cleaningServiceId):
        self.__id = id
        self.__userId = userId
        self.__cleaningServiceId = cleaningServiceId
    # GET    
    def getId(self):
        return self.__id
    def getUserId(self):
        return self.__userId
    def getCleaningServiceId(self):
        return self.
    # SET
    def setId(self,newId):
        self.__id = newId
    def setUserId(self,newUserId):
        self.__userId = newUserId
    def setCleaningServiceId(self, newCleaningServiceId):
        self.__cleaningServiceId = newCleaningServiceId

    def __str__(self):
        return '"{}","{}","{}"'.format(str(self.getId()),str(self.getUserId()),str(self.getCleaningServiceId()))
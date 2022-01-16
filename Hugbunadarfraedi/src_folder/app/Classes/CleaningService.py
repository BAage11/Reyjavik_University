class CleaningService:
    """ class that holds information about a certain cleaning service """
    def __init__(self,id,userId,hourlyRate,weekdays):
        """ Initialize the class with nessesary information """
        self.__id = id
        self.__userId = userId
        self.__hourlyRate = hourlyRate
        self.__weekdays = weekdays

    # GET methods to get instance information
    def getId(self):
        return self.__id
    def getUserId(self):
        return self.__userId 
    def getHourlyRate(self):
        return self.__hourlyRate
    def getWeekdays(self):
        return self.__weekdays

    # SET methods to set instance information
    def setId(self,newId):
        self.__id = newId
    def setuserId(self,newUserId):
        self.__userId = newUserId
    def setHourlyRate(self,newHourlyRate):
        self.__hourlyRate = newHourlyRate
    def setWeekdays(self,newWeekDays):
        self.__weekdays = newWeekDays

    # String method that puts the instance to csv friendly format
    def __str__(self):
        return '"{}","{}","{}","{}"'.format(str(self.getId()),str(self.getUserId()),self.getHourlyRate(),self.getWeekdays())
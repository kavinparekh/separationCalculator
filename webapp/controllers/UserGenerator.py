__author__ = 'kavinparekh'
from webapp.controllers.Neo4JController import Neo4JController
from random import randint


class UserGenerator:

    @staticmethod
    def createUsers(numOfUsers,loadFactor):
        USERNAME_CONSTANT_STRING = "User number "
        dbConnector = Neo4JController()
        for i in range(1,numOfUsers+1):
            personName = USERNAME_CONSTANT_STRING+str(i)
            dbConnector.addUser(personName)
        for i in range(1,numOfUsers+1):
            personName = USERNAME_CONSTANT_STRING+str(i)
            print 'now started for' + str(i)
            friends = set()
            friends.add(i)
            for j in  range(0,loadFactor):
                friendId = i
                attempts=0
                while(friendId in friends and attempts < 100):
                     #print friends
                     friendId = randint(1,numOfUsers)
                     #print friendId
                     attempts+=1
                if(attempts==100):
                    continue
                friends.add(friendId)
                friendName = USERNAME_CONSTANT_STRING+str(friendId)
                dbConnector.addConnection(personName,friendName)
                dbConnector.addConnection(friendName,personName)

    @staticmethod
    def deleteAllUsers():
        dbConnector = Neo4JController()
        dbConnector.deleteGraph()





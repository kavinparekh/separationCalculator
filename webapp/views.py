from django.shortcuts import render
from webapp.controllers.Neo4JController import Neo4JController
from webapp.controllers.UserGenerator import UserGenerator

from webapp.exceptions.NotConnected import NotConnected
# Create your views here.

def showIndexPage(request):
    return render(request, 'webapp/index.html')

def findDistance(request):
    try:
        fromNodeName = request.GET.get("fromNodeName")
        toNodeName = request.GET.get("toNodeName")
        distanceBetweenNodes = Neo4JController().findDistance(fromNodeName,toNodeName)
    except NotConnected:
        return render(request, 'webapp/showDistance.html',{'distance':'infinite (Not connected)','fromNodeName':fromNodeName,'toNodeName':toNodeName})
    except (ValueError,TypeError),arg:
        return render(request, 'webapp/errorWithInput.html',{'errorMessage':'Usage /findDistance?fromNodeName=<personName>&toNodeName=<toPersonName>'})
    return render(request, 'webapp/showDistance.html',{'distance':distanceBetweenNodes,'fromNodeName':fromNodeName,'toNodeName':toNodeName})

def generateUsers(request):
    try:
        numOfUsers = request.GET.get("numOfUsers")
        loadFactor = request.GET.get("loadFactor")
        numOfUsers = int(numOfUsers)
        maxConnectionsPerUser = int(loadFactor)
        UserGenerator.deleteAllUsers()
        UserGenerator.createUsers(numOfUsers,maxConnectionsPerUser)
    except (ValueError,TypeError),arg:
        return render(request, 'webapp/errorWithInput.html',{'errorMessage':'Usage /generateUsers?numOfUsers=<numOfUsers>&loadFactor=<loadFactor>'})
    return render(request, 'webapp/ok.html')

def deleteAllUsers(request):
    UserGenerator.deleteAllUsers()
    return render(request, 'webapp/ok.html')



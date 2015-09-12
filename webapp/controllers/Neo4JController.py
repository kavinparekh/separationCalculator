__author__ = 'kavinparekh'
from py2neo import Graph
from webapp.exceptions.NotConnected import NotConnected

class Neo4JController:

    def __init__(self):
        self.graph = Graph("http://localhost:7474/db/data/")

    def execute(self,query):
        return self.graph.cypher.execute(query)

    def findDistance(self,fromNodeName,toNodeName):
        try:
            #records = self.graph.cypher.execute("MATCH p =shortestpath((a:Person)-[r*]-(b:Person)) WHERE a.id IN ["+queryString+"] AND b.id IN ["+queryString+"] RETURN p")
            records = self.graph.cypher.execute("MATCH p =shortestpath((a:Person)-[r*]-(b:Person)) WHERE a.name = '"+fromNodeName+"' AND b.name= '"+toNodeName+"' RETURN  length(p)")
            print "MATCH p =shortestpath((a:Person)-[r*]-(b:Person)) WHERE a.name = '"+fromNodeName+"' AND b.name= '"+toNodeName+"' RETURN length(p)"
            print records
            record = records[0]
            separation = record[0]
            return separation
        except IndexError:
            raise NotConnected('Input nodes are not connected.')

    def getNodeIdFromName(self,name):
        records = self.graph.cypher.execute("MATCH (a:Person) WHERE a.name = '"+name+"' return a")
        record = records[0]
        table = record[0]
        return table.properties['id']

    def getAllNames(self):
        records = self.graph.cypher.execute("MATCH (a:Person) return a")
        record = records[0]
        table = record[0]
        return table.properties['id']

    def deleteGraph(self):
        records = self.graph.cypher.execute("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r;")

    def addUser(self,name):
        records = self.graph.cypher.execute("CREATE (n:Person { name : '"+name+"'})")

    def addConnection(self,fromNodeName,toNodeName):
        fromNodeId = self.getNodeIdFromName(fromNodeName)
        toNodeId = self.getNodeIdFromName(toNodeName)
        print 'from '+fromNodeName+' to '+toNodeName
        self.graph.cypher.execute("MATCH (from:Person),(to:Person) "
                                  +" WHERE to.name ='"+toNodeName+"'"
                                  +" and from.name ='"+fromNodeName+"'"
                                  +" CREATE UNIQUE (from)-[r:KNOWS]->(to)"
                                  +" ;")






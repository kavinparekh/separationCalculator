# separationCalculator

This is a django project which uses Neo4J to calculate the separation distance between two users. 

1)To use this you need to first generate a set of users using a request like 

127.0.0.1/generateUsers?numOfUsers=$NUM_OF_USERS&loadFactor=$LOAD_FACTOR

For eg.
127.0.0.1/generateUsers?numOfUsers=1000&loadFactor=20

This request will create a 1000 users with names like "User number 1", "User number 2" and so on...
Load factor is the average number of connections each user should have.


2) To find the distance between two users you should send a request like 

http://127.0.0.1:9999/findDistance?fromNodeName=$FROM_USER_NAME&toNodeName=$TO_USER_NAME

For eg.

http://127.0.0.1:9999/findDistance?fromNodeName=User%20Number%201&toNodeName=User%20Number%205





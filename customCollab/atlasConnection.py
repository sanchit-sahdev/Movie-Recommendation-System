import csv
from pymongo import MongoClient 
from SimpleUserCF import hello

client = MongoClient("mongodb+srv://admin:admin@moowe-ismxx.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database("moowe")

userLikes = db.userlikes
userRecc = db.userrecs
userLikesList = list(userLikes.find())
userReccList = list(userRecc.find())

#making convenient dict {userID : list of movies the user likes}
userLikesDict = {}
movieIDs = []
for i in userLikesList:
    firstMovList = (i["movies"])
    userID = (i["userID"])
    for j in firstMovList:
        movieID = (j["movieID"])
        movieIDs.append(int(movieID))
        userLikesDict[userID] = movieIDs
    movieIDs = []

print (userLikesDict, "\n")

#adding this data to a csv file 
for user, movie in userLikesDict.items():
    for i in movie:
        addCSV = [str(user), str(i), '5', '1']
        with open("ratings.csv", "a", newline ='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(addCSV)
        csvFile.close()

#making reccs for users
for i in userReccList:
    testSubject = i["userID"]
    rs = hello()
    finalRecc = rs.getRecc(testSubject)
    
    print ("Recomendations for User", testSubject, ":", finalRecc)
    print ("\n"*2)
    
    reccUpdate = {
                  "movies" : finalRecc
                 }
    
    userRecc.update_one({"userID": testSubject}, {"$set": reccUpdate})


    
    
    
    





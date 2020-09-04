from pymongo import MongoClient 

client = MongoClient("mongodb+srv://admin:admin@moowe-ismxx.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database("moowe")

userLikes = db.userlikes
userLikesList = list(userLikes.find())

userRecc = db.userrecs
userReccList = list(userRecc.find())

users = db.users
usersList = list(users.find())


userFriends = db.userfriends
userFriendsList = list(userFriends.find())

userFriendsRecs = db.userfriendrecs
userFriendsRecsList = list(userFriendsRecs.find())


"""
print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
for i in userLikesList:
    print (i)
    print ("\n")
print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


for i in userLikesList:
    print (i)
    print ("\n")
"""

friendemail = []
for i in userFriendsList:
    friends = i["friends"]
    for j in friends:
        friendemail.append(j["email"])
        
emailtoID = {}
for i in usersList:
    emailtoID[i["email"]] = str(i["_id"])


for j in userFriendsList:
    testSubject = j["id"]
    print ("Test Subject:", testSubject)
    friends = j["friends"]
    
    
    friendID = []
    for k in friends:
        friendemails = k["email"]
        friendid = dict(users.find_one({"email":friendemails}))
        friendFinalID = str(friendid["_id"])
        friendID.append(friendFinalID)
    
 
    
    friendLikes = []
    for l in friendID:
        for m in userLikesList:
            if str(m["userID"]) == str(l):
                friendlikemovies = list(m["movies"])
                for n in friendlikemovies:
                    friendlikesmovieID = n["movieID"]
                    friendLikes.append(friendlikesmovieID)
    
    
    
    userLikesmovies = []
    
    for o in userLikesList:
        if str(o["userID"]) == str(testSubject):
            ownmovies = list(o["movies"])
            for p in ownmovies:
                ownmoviesID = p["movieID"]
                userLikesmovies.append(ownmoviesID)
    
    
     
    finalRecc = []
    
    for q in friendLikes:
        if q in userLikesmovies:
            None
        else:
            finalRecc.append(q)
    
    
    
            
    

    
    finalRecc = list(dict.fromkeys(finalRecc))
    print (testSubject, ":", finalRecc)
    
    
    reccUpdate ={
                    "movies" : finalRecc
                }
    print (reccUpdate, "\n")
        
    userFriendsRecs.update_one({"userID": testSubject}, {"$set": reccUpdate})
    

            
    

    

    

    
    
    

        

# a dictionary is like a list of variables

# key : value pairs 

greg = {
    "name" : "greg",
    "gender" : "male",
    "height" : "Tall",
    "Job" : "developer"
}

# print greg["name"]
# print greg["gender"]

# make new dict

zombie = {} #dictionary
zombies = [] #list
#zombies.append()

# attributes MUST BE A STRING
# zombie[attribute] = value
zombie['weapon'] = "fist"
zombie['health'] = 100
zombie['speed1'] = 10

print zombie
print zombie['weapon']

for key,value in zombie.items():
    print "Zombie has a key of %s with a value of %s" % (key, value)

# in our game, poor zombie loses his weapon (arm falls off)
# we need to remove his weapon key

del zombie['weapon']
print zombie

is_nighttime = True
if(is_nighttime == True):
    zombie['health'] += 50

# put lists and dictionaries together
zombies = []
zombies.append({
    "name" : "hank",
    "weapon" : "baseball bat",
    "speed" : 10
})

# dictionaries that are appended print in most efficient order according to python

zombies.append({
    "name" : "willie",
    "weapon" : "axe",
    "speed" : 3,
    "victims" : [
        "squirrel",
        "rabbit",
        "racoon"
    ]
})


print zombies[0]

# this will get the first zombie in zombies weapon

print zombies[0]["weapon"]

# this will get the second victim, in the second zombies list of victims

print zombies[1]["victims"][1]
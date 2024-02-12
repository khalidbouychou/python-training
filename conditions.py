

note = 14

if note > 15:
    print("excellent")
elif note > 13:
    print ("assez bien")
elif note >= 10:
    print("passable")
else:
    print ("desole rak sa9et")

#ternary operator

note = 9.9
message = "success" if note >= 10 else "failure"
print (message)
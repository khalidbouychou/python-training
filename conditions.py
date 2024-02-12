

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

#operator conmparison  and not or
haveacc = True
solvable= True

if haveacc and solvable:
    print("have credit")
else:
    print("you cant")

#------------------------

username ="khbouych"
password =123
admin = True
msg = "welcome" if (username =="khbouych" and password ==123) or admin else "sign up"
print (msg)
msg = "welcome" if not admin else "sign up"
print (msg)
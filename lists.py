tab = ["abdo","adil","khalid"]
tab = ["abdo",False,2003]

#add delete from list

notes = [10 , 2 , 3]
notes.append(100)#addback
print(notes)
notes.extend([100,4,5])#add multipeles
print(notes)
notes.remove(100)
print(notes)
print("accessing -------------")
notes = [10,2,3,5,10,2,88,100,55,33]
print(notes[-8])
print(notes[2])

print("-"*20)
#slicing list
notes = [10,2,3,5,10,2,88,100,55,33]
print(notes[0:3])
print(notes[0:-1])
print(notes[1:-1])
print(notes[1:])
print(notes[:-1])
print(notes[0:-2:])
print(notes[0:-2:2])
print(notes[1:-2:2])
print(notes[::-1])
#[start:stop:step]
name = "khalid"
print(name[::-1])
#--------handling list ---------
tab = ["abdo","adil","adil","khalid"]
print(tab.index("adil"))
print(tab.count("adil"))
print(sorted(tab))
tab.sort()
print(tab)
tab.reverse()
print(tab)
print("pop" + "----"*20)
tab.pop(2)
print(tab)
tab.pop() #pop last element
print(tab)

print("join" + "----"*20)
tab = ["abdo","adil","adil","khalid"]
res = ""

for info in tab:
    res += info+" "
print (res)
res = " ".join(tab)
res = "-".join(tab)
print (res)
print("split" + "----"*20)
tab = "salam cv hani"
res = tab.split(" ")
tab = "salam , cv , hani"
res = tab.split(", ")
print(res)
print("search" + "----"*20)
tab = ["abdo","adil","adil","khalid"]
tabb = " adil adil khalid"
res = "basma" in tab #false
res = "khalid" in tab #true
res = "basma" not in tabb #true
res = "khalid" not in tabb#false
print(res)


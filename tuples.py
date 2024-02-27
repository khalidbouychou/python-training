

#a tuple is an ordered sequence of values. The values can be repeated, but their number is always finite. A tuple is often represented by a comma-delimited list whose values are enclosed in parentheses, although they're sometimes enclosed in square brackets or angle brackets.


#declaration

notes = (10,8,9)#tuple --> mode read
# notes = [10,8,9,10]#list ---> accept crud

x,z,y = notes
print(notes)
print(x,z,y)

#The key difference between tuples and lists is that while tuples are immutable objects, lists are mutable. This means tuples cannot be changed while lists can be modified

#------ cast tuple to list ----

#tuple to list
notes = (10,8,9)
nnotes = list(notes)
print(nnotes)

#list to tuple

notes = [10,8,9]
nnotes = tuple(notes)
print(nnotes)
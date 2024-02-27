

#The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter

notes= [
    ("khalid",22),
    ("meriem",21),
    ("farah",16),
]

mynotes = []

mynotes = list(map(lambda item : item[1],notes))
print(mynotes)
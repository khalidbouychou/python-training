

#The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

notes= [
    ("khalid",22),
    ("meriem",21),
    ("farah",10),
]

mynotes = filter(lambda item : item[1] > 15 , notes)
print(list(mynotes))
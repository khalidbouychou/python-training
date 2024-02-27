

#A lambda function is a small anonymous function.A lambda function can take any number of arguments, but can only have one expression

#syntax : lambda arguments : expression

notes= [
    ("khalid",22),
    ("meriem",21),
    ("farah",16),
]

notes.sort(key=lambda item : item[1])
print(notes)
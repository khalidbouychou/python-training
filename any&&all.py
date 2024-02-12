notes  = [16 ,18,11,15,9,14,20,8,10]

res = False
for note in notes:
    if note >= 18:
        res = True
        break
print(res)
print("**"*20)

res = any([note >= 18 for note in notes])
print(res)
res = all([note < 10 for note in notes])
print(res)
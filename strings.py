#sigle qoutes
platform = "1337 khouribga"

#more lines
platformm = """salam
cv
hani
"""
print (platformm[0:6])#--->salam
print (platformm[:2])#---->sa
print (platformm[-6:-1]) #---> hani


test = 'salam "cv"'
#\' #\" #\n #\r #\b #\t #\r #\\...
test = "salam \'salam'"
print (test)


#contatination

khalid = "khalid"
bouychou = "bouychou"
age = 26

formatted_string = f"My name is {khalid} {bouychou} and I am {age} years old."
print(formatted_string)

print ("--"*20)

#methods strings

variable = "salam cv"

print (len(variable))
print (variable.upper())
print (variable.title())
print (variable.find("cv"))
variable = "     salam      "
print (variable.lstrip())
print (variable)
print (variable.rstrip())
variable = "salam"
print(variable.replace("sa","zz"))



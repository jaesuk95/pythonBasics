# type() function is used to know which class a variable belongs to or a value belongs to
a = 5
print(a, "is of type", type(a)) # <- this type will define integer

a = 2.0
print(a, "is of type", type(a)) # <- define float

a = "i am string"
print(a, "is of type", type(a)) # <- String,,

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))

print("*********************")

a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[0] = ", a[0])

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

print("*********************")

tuple = (5,'program', 1+3j)

print(type(tuple))

# t[1] = 'program'
print("t[1] = ", tuple[1])  # <- you are only printing a part of tuple // quite unnecessary

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", tuple[0:3])

print("*********************")

s = "This is a string"
print(s)
s = '''<A multiline
string>'''
print(s)

print("*********************")

set = {5,2,3,1,4,1}
# set, but in order // different from java,
# printing set variable
print("a = ", set)

# data type of variable a
print(type(set))

print("*********************")
# key value in python

d = {1:'value','key':2}
print(type(d))

print("d[1] = ", d[1])
print("d['key'] = ", d['key'])





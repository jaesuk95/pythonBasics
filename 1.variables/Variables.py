# automatically detects number -> int
number1 = 10
print(number1)

number2 = 1.1
print(number2)

# note: StringFormat numbers can be calculated - different from Java
print(number1 + number2)
# result :

# String format
website = "apple.com"
print(website)

# overriding string
website = "google.com"
print(website)

# Float Literal
float_1 = 10.5
float_2 = 1.5e2

# Complex Literal
x = 3.14j

print(float_1, float_2)
print(x, x.imag, x.real)

print("*****************")

strings = "This is Python"
char = "C"
multiLine_str = """<This is a multiLine String
 with more than one line code>"""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiLine_str)
print(unicode)
print(raw_str)

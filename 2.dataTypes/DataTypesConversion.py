num_int = 123
num_float = 1.23

num_new = num_int + num_float

print("dataType of Num_int: ", type(num_int))
print("dataType of Num_int: ", type(num_float))

# when int + float calculation is proceeded, float will take over
print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

print("**************************")

num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str:",type(num_str))

# print(num_int+num_str) # this will not work because string and integer cannot be added together therefore wrap it
num_str = int(num_str)  # in java we use "Long.valueOf()" or Integer.valueOf(), or Integer.parseInt()
print(num_int + num_str)
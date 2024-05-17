#indntation error
#if 8 > 2:
#print("greter then ")

# right way to code 
if 8 > 2 :
    #print("greter then")
    #print("second ")


# ----> this is the comment line -------------------------------------->>>

#variable declaration
    x = 6
    y = "Python" 
    z = 'this also use'
 

#print(x,y,z)

# multi line comment 
"""
    This is used to multi line comment 
    for python 
    prigramming
"""

# vriable type casting in python ------------------------------------------------->>>

x = str("3")
y = int(12)
z = float(12)

#print(x,y,z)
#print(x+ " ",y+z)


#type checking using type() --------------------------------------------------------------->>>

x = 7
y = "python"
z = 12.7

#print(type(x))  # <class 'int'>
#print(type(y))  #<class 'str'>
#print(type(z))  #<class 'float'>

# Python is case-Sensitive

a = "hello"  # or
A = 12       # both are not same 

#print(a,A)

# invalid variable name creation   ----------------------------------------------------->>>

"""
2myvar = 2
my-var = "hey"
my var = 12.9

"""
#three Type of casting  ----------------------------------------------------------------->>>

# Camel case 
myVariableName =  12       

# pascal case 
MyVariableName = 21

# Snake Case 
my_variable_name = 23

#print(myVariableName,MyVariableName,my_variable_name) # three are deferent variables

# Assign values for variables   -------------------------------------------------------------------------->>> 

#Many values to multipul variables

x,y,z = "black","blue","orenge"

#print(x,y,z)

#v  # Name Error : name 'v' not defined
#print(v)

# one value to  multipule variables 

x = y = z = "Obito"

#print(x,y,z)

# unpack a collction

colors = ["black","white","red"]
x,y,z = colors

#print(colors)  # >>> ['black','white','red']
#print(x,y,z)   # >>> black white red

# string concating useting +

x = "python "
y = "is "
z = "awesome"

#print(x+y+z)  # or 
concat = x + y + z
#print(concat) # both are same

# number and string is dosn't concat 
x = 2
y = "number"

#print(x + y) # TypeError : unsupported operand type(s) for + 'int' and 'str'

# global variable 


x = "i'm x"

def myfun():
    print("function is " + x)

#myfun()

def my2fun():
    x = "awesome" # the x = "i'm x" is override for the inside function x = "awesome"
    print("python is " + x)

#my2fun()
#print("x is " + x) # >>> x is i'm x

# slove the problem

def sol():
    global x
    x = "awesome"
    print("solve problem is " + x)

#sol()
#print(" x --!" + x) # >>> x --! awesome


"""
you declar the inside the function global x 
you will using the same  value in outter the function

"""




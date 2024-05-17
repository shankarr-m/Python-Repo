# Pyhton Date types

"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

"""

x = 6 
#print(type(x))  # >>> int 

x = "Hello Python" 
#print(type(x))  # >>> str

x = 12.7
#print(type(x))  # >>> float

x = 19072j
#print(type(x))  # complex

x = [1,9,98,97]
#print(type(x))  # list

x = ("orang","banana","mango")
#print(type(x))  #tuple

x = range(6)
#print(type(x))  # range

x = {"name":"john","age":21} 
#print(type(x))  #dict

x = {"apple","orange","cherry","apple"}
#print(type(x))  # set

x = frozenset({"apple","orange","cherry","apple"})
#print(type(x)) # froznset

x = True
#print(type(x))  # bool

x = b"hey" 
#print(type(x))  # byte

x = bytearray(6)
#print(type(x))  # bytearray

x = memoryview(bytes(6))
#print(x,type(x)) #memoryview

x = None
#print(type(x))

# Other way to create the datatype variables

x = int(2)
x = str("hey")
x = float(12)
x = complex(12j)
x = list(("apple","banana","orange"))
x = tuple(("apple","banana","orange"))
x = range(9)
x = dict(name="john",age=21)
x = set(("apple","banana","orange"))
x = frozenset(("apple","banana","orange"))
# only 0 are () and "" empty is False by the way all are True  
x = bool("")
#print(x)
x = bytes(6)
x = bytearray(8)
x = memoryview(x)
#print(x)
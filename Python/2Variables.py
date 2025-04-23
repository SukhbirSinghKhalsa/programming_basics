"""
variables

# Variables are reserved memory blocks which can store some value in memory that can be reused again and again
# Mutiple datatypes used are used in python and are loosely typed
# meaning we can change the type of variables anytime say number =10 intially can be number = "Ten" later on

Primitive Datatypes
1 number - int, float
2 string
3 boolean

Complex Datatype
1 List
2 Tuple
3 Set
4 Dictonary
5 complex number
6 Range
"""

contactNo = 8766814548
pi = 3.14
shortName = "SSK"
isMad = True

lovesTo = ["automate stuff","play chess"]
forever = ("crazy","bikelover","singer")
uniqueness = {"silent", "thinker", "can stay alone"}
knows = {"IAC": "Terraform", "Cloud":"Azure", "Containerization":["Docker","Kubernetes"]}
someMath = 4 + 5j



print("Number integer",contactNo)
print("Number float",pi)
print("String", shortName)
print("Bolean", isMad)
print("List", lovesTo)
print("Tuple", forever)
print("Set", uniqueness)
print("Dictionary", knows)
print("Complex Number", someMath)


"""
type(variable)
to check the type of variable we use type function with variable as an argument to it
"""

print("Type of contactNo",type(contactNo))
print("Type of pi", type(pi))
print("Type of shortName", type( shortName))
print("Type of isMad", type( isMad))
print("Type of lovesTo", type( lovesTo))
print("Type of forever", type( forever))
print("Type of uniqueness", type( uniqueness))
print("Type of knows", type( knows))
print("Type of someMath", type( someMath))


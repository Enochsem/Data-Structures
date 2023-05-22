# __str__() and __repr__()

import datetime  #datatime.datetime has a built in representation of __str__() and __repr__() 

mydate = datetime.datetime.now()

# __str__() direct usage
print("__str__() : ",mydate.__str__()) # return a human readable string representation
print("str() : ",str(mydate)) 
'''# the str() calls __str__() to return human readable representation of an object'''

# __repr__() direct usage
print("__repr__() : ",mydate.__repr__()) # return a more imformation rich string representation of an object(datetime) that can be used to recreate the object
print("repr() : ",repr(mydate))
"""# the repr() calls __repr__() to return information"""

mydate2 = eval(repr(mydate)) #recreating and executing the object
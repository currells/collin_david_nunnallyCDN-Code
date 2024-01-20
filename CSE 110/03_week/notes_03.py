#Str is in quotes
_str = "1234567890"
#int is number w/o quotes
_int = 456789
#float is anything that needs a decimal
_float = 753.369
#boolean is True/False
_bool = False

"""
Won't use these that much in class, but may use them in stretch
challenges
"""
# # list is being able to use any data type
# __list = [4789, 369.258, "asdfe"] #Array
# # Like array, but once created, it can't be changed
# _tup = (147,258.25,"adsfg")
# _dictionary = {} #Object

eggs = input("How many eggs do you have left? " )
eggs = str("eggs")

print(f"{type(eggs)} {eggs * 2}")


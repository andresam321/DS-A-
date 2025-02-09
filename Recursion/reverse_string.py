# write a function takes a string as an arguement, the function should return the string with its character in reverse order
# you must do this recursively 

# def reverse_string(string):
#     if len(string) == 0:
#         return ""
#     # print(reverse_string(string[1:]))
# # string = "abc"

# #                       "abc"         +      ""
# #                       "bc"          +        "a"
# #                       "c"           +       "b"
# #                       ""            +      "c"
# #                        ""            +     ""

# # c b a
# # "abc"
#     result = reverse_string(string[1:]) + string[0]

#     return result


# print(reverse_string("hello")) # -> "olleh"












###string as an arugment , character in reverse order , recursively

### def reverse_string(string):

# base case 

# if len(string) == 0:
# return ""


# result = reverse_string([1:]) + reverse_string[0]

# return result 

# string = "stopwatch"

#         "stopwatch" + ""

#         "topwatch" + "s"

#         "opwatch"  + "t"

#         "pwatch"  + "o"

#         "watch"  + "p"

#         "atch"  + "w"

#         "tch"  + "a"
#         "ch"  + "t"
#         "h"  + "c"
#         ""  + "h"

# hctawpots
##

def reverse_string(string):
    if len(string) == 0:
        return ""
    
    result = reverse_string(string[1:]) + string[0]

    return result


print(reverse_string("stopwatch")) # -> "hctawpots"



# takes in a list of strings and returns the total langth of trings
###

def sum_of_lengths(strings):
    if len(strings) == 0:
        return 0
# new frame
  #  [4,2,7,5   + 5 + 7 + 12 + 2 + 14 + 4 = 18   
  # 
  # recursively checks every index of strings then adds it to the stack once it unwinds it adds it because of our base case 

#           4      +      ["cat,"purple"]

#           3      +       ["purple"]

#           6      +        []


#           6       +       0 = 6

#           6       +       3 = 9

#           9       +       4 = 13
    print(len(strings[0]))
    result = len(strings[0]) + sum_of_lengths(strings[1:])
    print(len(strings[0]))
    return result 
## stack lifo , 0 goat > 1 cat  > 2 purple 
##              len(4) > len(3) > len(6)

## new
#  top     end
#   4 
## ___ ___ ___

print(sum_of_lengths(['goat', 'cat', 'purple'])) # -> 13
# print(sum_of_lengths(['bike', 'at', 'pencils', 'phone'])) # -> 18

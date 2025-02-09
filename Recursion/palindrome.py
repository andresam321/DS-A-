## write a func name palindrome takes in a "string"

## returns a boolean indicating whether or not the string is the same forwards and backwards 



## def palindrome(string):
## if len(string) == 0:
# return 0 
## s = 0 
## also just make a while 
## while s < len(string)
## 
#make 2 seperated arrays and push them when theyre getting added to the frame and when its unwinding?
## forward = []
## backwards = []
## forward.append(string)

def palindrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
   
    if  string[0] != string[-1]:
        return False
    
    return palindrome(string[1:-1])
## "y"
print(palindrome("kayak")) # -> True


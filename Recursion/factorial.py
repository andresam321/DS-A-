### n numbers returns factorial is less than or equal to n such # 5 4 3 2 1
## n = 0 return 1 
## return n * factorial(n - 1 );



def factorial(n):
  if n == 0:
    return 1
  print(f"inside",n)
  return n * factorial(n-1)

## 3 is added to the stack then 2 is added , then 1 , then 1 

## 1 * 1 , 2 * 1 , 3 * 2 = 6

#   3 * 2 = 6
## ___
#   2 * 1
## ___
#   1  * 1
## ___
#   
## ___


print(factorial(3)) # -> 6
print(factorial(6) )# -> 720
print(factorial(18)) # -> 6402373705728000
print(factorial(1) )# -> 1
print(factorial(13)) # -> 6227020800
print(factorial(0)) # -> 1

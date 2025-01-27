def factorial(n):#factorial(3) # -> 3 , 2
  if n == 0:
    return 1
  print(f"inside",n)
  return n * factorial(n-1)
  print(f"outside",n)


factorial(3) # -> 6
factorial(6) # -> 720
factorial(18) # -> 6402373705728000
factorial(1) # -> 1
factorial(13) # -> 6227020800
factorial(0) # -> 1

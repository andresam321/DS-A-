def fib(n):
  memo = {}
  return _fib(n, memo)



def _fib(n, memo):
  if n == 0 or n == 1:
    return n
  if n in memo:
    return memo[n]
    
  memo[n] = _fib( n - 1, memo) + _fib(n - 2, memo)
  print(memo[n])
  return memo[n]


fib(0); # -> 0
fib(1); # -> 1
fib(2); # -> 1
fib(3); # -> 2
fib(4); # -> 3
fib(35); # -> 9227465
fib(46); # -> 1836311903

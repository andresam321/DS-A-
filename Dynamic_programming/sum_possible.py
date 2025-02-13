def sum_possible(amount, numbers):
  memo = {}
  return _sum_possible(amount, numbers, memo)

# sum_possible(13, [6, 2, 1]) # -> True
def _sum_possible(amount, numbers, memo):
    if amount in memo:
        print(f"Memo hit: {amount} -> {memo[amount]}")
        return memo[amount]
    if amount == 0:
        print(f"✔ Found valid sum: {amount}")
        return True
    if amount < 0:
        print(f"❌ Invalid (negative): {amount}")
        return False
    print(f"Checking amount: {amount}")
    for num in numbers:
        print(f"  Trying {num}: {amount} - {num} = {amount - num}")
        print(f"  Trying {num}: {amount} - {num} = {amount - num}")
#                        13 - 2 , 11 - 2 , 9 - 2, , 1
        if _sum_possible(amount - num, numbers, memo):
            memo[amount] = True
            print(f"✔ Storing in memo: {amount} -> True")
            return True  # Exit early if we find a valid sum

    memo[amount] = False
    print(f"❌ Storing in memo: {amount} -> False")
    return False
sum_possible(15, [6, 2, 10, 19]) # -> False

sum_possible(8, [5, 12, 4]) # -> True, 4 + 4


sum_possible(13, [6, 2, 1]) # -> True


sum_possible(13, [6, 2, 1]) # -> True
sum_possible(12, []) # -> False

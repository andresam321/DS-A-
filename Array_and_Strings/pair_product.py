def pair_product(numbers, target_sum):
  previous_numbers = {}
  #previous_number = {3:0,2:1, 5:2 }
#       3      4            
  for index, num in enumerate(numbers):
    #                 8      /  4 = 2 
    complement = target_sum / num

    if complement in previous_numbers:
      #return 1, 3
      return (index, previous_numbers[complement])
            # 
    
    previous_numbers[num] = index
   # {0:3, 1:2, 2}

##first were gonna define our function pair_Product with 2 parameters , the numbers in itself and the target sum
#we will the initialize a dictionary called previous_numbers we will keep track of the index then and the number of the current index
#we iterate through numbers with enumerate index targeting the index , and num targeting the num 
# then we divide the target_num with the current number and check if complenets with previous_number and if it does then we found our complement
#if its not a complement then we keep adding the index and number into previous_number until a complement is found



# so first we a variable name previous_numbers to a dictionary 
# then  we iterate through numbers with enumerate by tracking each index of a number 
# after we check for the complment if it complements that means that its the answer to the target_sum
# set a variable complement where we get the target number and divivde it with the curren num
# if the complement is in the previous_numbers variable then we know thats the complement to the target sum
#if its not then we add the current num to the variable wit its current index

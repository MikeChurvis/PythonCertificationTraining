def is_prime(num):
    
    # Only check positive numbers.
    if num < 1:
        return False
    
    # 1, 2, and 3 are prime.
    if num < 4:
        return True
        
    # No number can be evenly divided by a number greater than itself / 2
    for possible_factor in range(2, 1 + num // 2):
        if num % possible_factor == 0:
          return False
          
    return True
        
    

for i in range(2, 21):
	if is_prime(i):
			print(i, end=" ")
print()

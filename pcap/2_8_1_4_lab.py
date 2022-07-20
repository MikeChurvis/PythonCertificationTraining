def read_int(prompt, min, max):
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            print('Error: wrong input')
            continue
            
        if user_input not in range(min, max + 1):
            print('Error: the value is not within permitted range (-10..10)')
            continue
        
        return user_input
        
v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)

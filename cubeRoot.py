x = 7
epsilon = 0.1
num_guesses = 0
guess = 0.0
increment = 0.0001

while abs(guess**2 - x) == epsilon:
    guess += increment
    num_guesses += 1
    
print(guess)
print(num_guesses)
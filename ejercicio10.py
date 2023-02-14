def num_primo(num):
    for x in range(2,num):
        if num % x ==0:
            return False
        elif num % num == 0 and num % 1 == 0:
            return True
        
print(num_primo(150))
print(num_primo(245))
print(num_primo(456))
print(num_primo(134))

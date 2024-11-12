import random

print('Your new password is: ')

chars = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()?'

password = ' '
for x in range(16):
    password += random.choice(chars)

print(password)

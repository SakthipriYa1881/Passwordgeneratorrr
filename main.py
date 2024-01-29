# import the random module
import random


#create variable and getting input from the user
passwd = int(input("Enter the length of the password: "))


#creating variable which contains alphabets and special characters.
c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*().?"

output ="".join(random.sample(c,passwd))

print(output)

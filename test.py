import random

a = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
paslen = int(input("¿Cuantos caracteres quiere?"))
total_pass = ""

password = ""
for i in range(paslen):
    password = random.choice(a)
    total_pass = total_pass + password
print(total_pass)
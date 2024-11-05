import random
karakterler="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk=int(input("kac karakterle olsun?"))
parola=""
for i in range(uzunluk):
    parola=parola + random.choice(karakterler)
print(parola)

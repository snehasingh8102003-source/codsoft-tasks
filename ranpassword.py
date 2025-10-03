import random
import string
def password_generater(length=12):
    if length<0:
        return ("password must be greater than 4 charactors")
    password=[random.choice(string.ascii_lowercase),
              random.choice(string.ascii_uppercase),
              random.choice(string.digits),
              random.choice(string.punctuation)]
    charactors=string.ascii_letters+string.digits+string.punctuation
    password += [random.choice(charactors) for _ in range(length - 4)]
    random.shuffle(password)
    return "".join(password)
user= int(input("enter desired password length: "))
print("your random password is: ", password_generater())
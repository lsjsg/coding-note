import random
def password():
    a=''
    for i in range(8):
        a+=chr(random.randint(32,126))
    print(a)
password()

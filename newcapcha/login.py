import random
from newcapcha import mark
from newcapcha.forpswd import Captcha


def login_fun():
    uppercase = [chr(j) for j in range(65, 91)]
    lowercase = [chr(j) for j in range(97, 122)]
    digits = [str(j) for j in range(10)]
    samples = uppercase + lowercase + digits
    us = input("Enter the username:")
    ps = input("Enter the password:")
    obj = Captcha(ps, us)
    c = obj.check_password()
    print("Login Form")
    u = input("Enter the username:")
    p = input("Enter the password:")
    while True:
        z = random.sample(samples, k=5)
        s = ""
        for i in z:
            s += i
        print("Type the captcha :", s)
       
        captcha = input()
        if s == captcha:
            if u == c["username"] and p == c["password"]:
                print(f"Welcome {u}")
                q = mark.marks()
                for s, m in q.items():
                    print(f"{s}\t:{m}".expandtabs(10))
            break
        else:
            print("Please try again")

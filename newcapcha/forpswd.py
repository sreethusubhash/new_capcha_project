class Captcha:
    def __init__(self, password="", username="") -> None:
        self.password = password
        self.username = username
        self.d = {}

    # def return_dict(self):
    #     return self.d

    def check_password(self):
        cnt = 0
        while cnt == 0:
            uppercase_check = lowercase_check = digits_check = specialchar_check = 0
            for i in self.password:
                if i.isupper():
                    uppercase_check += 1
                elif i.islower():
                    lowercase_check += 1
                elif i.isdecimal():
                    digits_check += 1
                else:
                    specialchar_check += 1
            if (
                uppercase_check >= 2
                and lowercase_check >= 3
                and digits_check >= 2
                and specialchar_check >= 1
            ):
                self.d["username"] = self.username
                self.d["password"] = self.password
                # print(self.d)

                cnt += 1

                if cnt:
                    # print(self.d)
                    return self.d

            else:
                us = input("Enter the username:")
                ps = input("Enter the password:")
                Captcha(ps, us)
                self.check_password()

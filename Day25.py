PROJECT BASED ON REGULAR EXPRESSION
-----------------------------------
Validation
----------

1.Mobile number
---------------
--> 10 digits init....

2.Password
----------
--> Cap,small,digit,special char,atleast 8 digit password

3.Mail
------
--> it should be end with @gmail.com


import re
class Validation:
    def mobile(self,mob):
        pat=r"^[6-9][0-9]{9}"
        if re.fullmatch(pat,mob):
            return "Valid Mobile number"
        else:
            return "Invalid Mobile number"
    def ss(self,password):
        pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$%^&*]).{8,}$"
        if re.fullmatch(pat,password):
            return "valid Password"
        else:
            return "Invalid Password"
    def email(self,gmail):
        pat=r".+@gmail.com"
        if re.fullmatch(pat,gmail):
            return "Valid email"
        else:
            return "Invalid email"
obj=Validation()
m=input("Enter your mobile number: ")
p=input("Enter Your Password: ")
e=input("Enter your email: ")
print(obj.mobile(m))
print(obj.ss(p))
print(obj.email(e))

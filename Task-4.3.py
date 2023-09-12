import random
import string
Length=int(input("Enter password length: "))
upper=str(input("Include uppercase letters?(yes/no): "))
lower=str(input("Include lowercase letters?(yes/no): "))
numbers=str(input("Include number?(yes/no): "))
characters=str(input("Include special characters?(yes/no): "))
var=''
if upper=='yes':
    var+=string.ascii_uppercase
if lower=='yes':
    var+=string.ascii_lowercase
if numbers=='yes':
    var+=string.digits
if characters=='yes':
    var+=string.punctuation
if not var:
    print("Atleast one character should be selected for generating a password")
else:
    password=''.join(random.sample(var) for i in range(Length))
    print(password)
        

    



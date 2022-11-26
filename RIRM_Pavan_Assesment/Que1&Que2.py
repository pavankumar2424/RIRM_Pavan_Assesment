# Que 1. WAP to check if the given contact number is valid or invalid using 
# regular expressions-

# Ans 1.

import re
 
def check(num): 
    patt = re.compile("(0|91)?[6-9][0-9]{9}")
    return patt.match(num)
 
num = input('Enter Phone number:')

if (check(num)):
    print("Your Number is Valid Phone Number.")    
else:
    print("Enter Number is Invalid Phone Number.")
 



# Que 2. WAP to get the Social Links, Email & Contacts details of a website 
# on user input.

# Ans 1.

# --------- Here I take Temporary Database ----------------

company = 'ful.io'
facebook = 'https://www.facebook.com/fulioTech/'
linkedin = 'https://www.linkedin.com/company/ful-io/'
email = 'ssupport@ful.io'
contact = '+1 343 303 6668'

# ---------  Temporary Database End ----------------

company_name = input('Enter any Company Name:')

if company_name.lower() == company :
    print('Social Links - ')
    print('FaceBook Link -', facebook)
    print('Linkedin Link -', linkedin)
    print('Email -', email)
    print('Conatct :', contact, sep='\n')
else:
    print('Enter Valid Company Name.')


print("Password Chacker Application".center(50, "*"))
import string
small = string.ascii_lowercase
capital=string.ascii_uppercase
symbol=string.punctuation
numbers=string.digits
while True:
    password = input("Enter the password :")
    if len(password)>=8:
            d={'small':False,'capital':False,'symbols':False,'numbers':False}
            for i in password:
                if i in small:
                    d['small']=True
                elif i in capital:
                    d['capital']=True
                elif i in symbol:
                    d['symbols']=True
                elif i in numbers:
                    d['numbers']=True
            if list(d.values()).count(True)==4:
                print('Password is Strong'.center(50, '-'))
                break
            else:
                print('Password is Not Strong')
                for i in d:
                    if d[i]==False:
                        print(i,'is Missing')
    else:
        print('Password is not Strong , As It has less than 8 Characters')
    
    

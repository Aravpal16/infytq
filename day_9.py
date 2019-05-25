#PF-Assgn-57
def check_prime(number):
    return number > 1 and all(number % i != 0 for i in range(2, number))
    
def rotations(num):
    rotated = []
    m = str(num)
    for i in m:
        rotated.append(int(m))
        m = m[1:] + m[0]
    return rotated

def get_circular_prime_count(limit):
    counter = 0 

    for number in range(1, limit):
        if all(check_prime(number) for number in rotations(number)): 
            counter += 1 
    return counter
#Provide different values for limit and test your program
print(get_circular_prime_count(1000))

#PF-Assgn-61
import re
def validate_name(name):
    if(len(name)!=0 and len(name)<=15 and name.isalpha()):
            return True
    else:
            return False

def validate_phone_no(phno):
    count = 0
    if(len(phno)==10 and phno.isdigit()):
        for i in range(1,len(phno)): 
            if (phno[i] == phno[i-1]): 
                count = count + 1 
        if(count!=len(phno)-1):
            return True
        else:
            return False
    else:
        return False

def validate_email_id(email_id):
    if(email_id.endswith(".com") and email_id.count("com")==1 and email_id.count("@")==1):
        if("gmail" in email_id or "yahoo" in email_id or "hotmail" in email_id):
            return True
        else:
            return False
    else:
        return False

def validate_all(name,phone_no,email_id):
    count = 0
    if(validate_name(name)):
        count = count + 1
    else:    
        print("Invalid Name")    
    if(validate_phone_no(phone_no)):
        count = count + 1
    else:    
        print("Invalid phone number")
    if(validate_email_id(email_id)):
        count  = count + 1
    else:    
        print("Invalid email id")
    if(count==3):
        print("All the details are valid")

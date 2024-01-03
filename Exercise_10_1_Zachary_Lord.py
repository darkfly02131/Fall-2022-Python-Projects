#Zachary Lord

def main():
    full_name = get_full_name()
    print()
    password = get_password()
    print()
    email = get_email()
    print()
    phone = get_phone_number()
    first_name = get_first_name(full_name)   
    print("Hi " + first_name + ", thanks for creating an account.")
    print("We'll text your confirmation code to this number: ",phone)
    
#Purpose: get the full name from the user
def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")
    
#Function: get the first name of the user
def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name
#Purpose: get the email of the user
def get_email():
    while True:
        email = input('Enter email address: ')
        at_index =email.find('@')
        dot_index = email.find('.', at_index)
        if at_index == -1 or dot_index == -1:
            print('Invalid email address:', email)
        else:
            return email
#Purpose: Get the phone number of the user.
def get_phone_number():
    while True:
        phone = input('Enter Phone Number: ')
        phone.strip()
        phone= phone.replace("-", "")
        phone= phone.replace(" ", "")
        phone.replace("(", "")
        phone= phone.replace(")", "")
        phone= phone.replace(".", "")
        phone_correct = phone.isdigit()
        if phone_correct == True and len(phone) == 10:
          phone= phone[:3] + "." + phone[3:6] + "." + phone[6:]
          return phone
        else:
            print('Please enter a 10-Digit Phone Number')
#Purpose:Get the password of the user.            
def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print("Password must be 8 characters or more \n" +
                  "with at least one digit and one uppercase letter.")
        else:
            return password
        
if __name__ == "__main__":
    main()

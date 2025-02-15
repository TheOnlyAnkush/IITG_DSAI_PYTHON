def validate_username():
    username = input("Enter a username: ")
    if (len(username)>=5):
        valid = True
        
        for char in username:
            if not (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 or 48 <= ord(char) <= 57):
                valid = False
                break
        
        if valid:
            print("Valid username.")
        else:
            print("Invalid username.")    
    else:
        print("Invalid username.")
validate_username()
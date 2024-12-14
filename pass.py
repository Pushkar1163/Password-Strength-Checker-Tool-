import re

def password_strength(password):
    """
    Checks the strength of a password based on various criteria.

    Criteria:
        - At least 8 characters long
        - Contains both uppercase and lowercase letters
        - Contains at least one number
        - Contains at least one special character (!@#$%^&*()-_+=)
    """
    
    strength_level = 0

   
    length_regex = r'.{8,}'
    uppercase_regex = r'[A-Z]'
    lowercase_regex = r'[a-z]'
    number_regex = r'[0-9]'
    special_char_regex = r'[!@#$%^&*()\-_=+]' # Allowed special characters

  
    if re.search(length_regex, password):
        strength_level += 1
    if re.search(uppercase_regex, password):
        strength_level += 1
    if re.search(lowercase_regex, password):
        strength_level += 1
    if re.search(number_regex, password):
        strength_level += 1
    if re.search(special_char_regex, password):
        strength_level += 1


    if strength_level <= 2:
        return "Weak"
    elif strength_level == 3:
        return "Moderate"
    elif strength_level == 4:
        return "Strong"
    else:
        return "Very Strong"

if __name__ == "__main__":
 
    password = input("Enter your password: ")

  
    strength = password_strength(password)

 # Display result
    print(f"Your password strength is: {strength}")
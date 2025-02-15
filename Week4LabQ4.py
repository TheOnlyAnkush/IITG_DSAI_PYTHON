def compare_string_length():
    # Prompt user to enter two strings
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    
    # Compare the lengths of the strings
    if len(string1) > len(string2):
        print("The first string is longer.")
    elif len(string1) < len(string2):
        print("The second string is longer.")
    else:
        print("Both strings are of equal length.")

# Call the function to compare the string lengths
compare_string_length()
try:
    input_string = input("Enter the string: ")
    if input_string == input_string[::-1]:
        print("The entered string is a palindrome")
    else:
        print("The entered string is not a palindrome")
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')

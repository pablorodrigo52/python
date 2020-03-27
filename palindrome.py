#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

word = input("Enter with a string: ").lower()

if (word == word[::-1]):
    print("Thats a palindrome!")
else:
    print("Not is a palindrome.")
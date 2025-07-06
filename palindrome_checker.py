

k = 1
while (k>0):
    
    user_input = input("Enter a word: ")

    if(user_input.isalpha() == True):
        reverse_input = user_input[::-1]

        if(user_input == reverse_input):
            print(f"{user_input} is a palindrome")
        else:
            print(f"{user_input} is a not palindrome")
    else:
        print(" Alphabets only" )


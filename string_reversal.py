def str_rev(a):
    
    save_rev = a[::-1]
    return save_rev

user_in = str(input("enter a string: "))

user_out = str_rev(user_in)
print(user_out)
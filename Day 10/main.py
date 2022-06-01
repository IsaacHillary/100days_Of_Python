def full_names(f_name, l_name):
    return f_name.title()+" "+l_name.title()

f_name = input("What is your first name?  ")
l_name = input("What is your last name?   ")
print(full_names(l_name=l_name, f_name=f_name))

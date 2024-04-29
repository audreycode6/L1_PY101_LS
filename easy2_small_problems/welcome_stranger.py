# Create a function that takes 2 arguments, a list and a dictionary. 
# The list will contain 2 or more elements that, when joined with spaces, 
# will produce a person's name. The dictionary will contain two keys, "title" and "occupation", 
# and the appropriate values. Your function should return a greeting that uses the person's 
# full name, and mentions the person's title.

# OPTIONAL: allow user to put in their own input at terminal 
# comment out if want to input args yourself
name = input("Enter your full name (ex. Jane Middlename Doe): ")
name_list = name.split(' ')

job = input("Enter your job (ex. Plumber): ")
title = input("Enter your title at your job (ex. Master): ")
job_dict = {'title': title, 'occupation' : job,}


def greetings(name_list, job_dict):
    if len(name_list) < 2: 
        return "Please enter your full name: first, last, etc. !"
    
    full_name_string = ' '.join(name_list) 

    return f"Hello, {full_name_string}! It's nice to meet a {job_dict['title']} {job_dict['occupation']}!"

# TEST
print(greetings(name_list, job_dict)) 


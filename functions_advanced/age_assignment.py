def age_assignment(*args, **kwargs):
    my_dict = {}
    for x in args:
        for k, v in kwargs.items():
            if x.startswith(k):
                my_dict[x] = v
    return my_dict


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
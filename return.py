def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age

dr3as_limit = allowed_dating_age(34)
bucky_limit = allowed_dating_age(27)
print("Dr3as can date girls", dr3as_limit, "or older")
print("Bucky can date girls", bucky_limit, "or older")
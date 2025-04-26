def greet_user(name):
    return f"Hello, {name}!"

print(greet_user("Huy"))

# def my_function_one(*kids):Dùng để gom nhiều tham số không tên (positional arguments) thành một tuple(*args)
#   print("The youngest child is " + kids[2])

# my_function_one("Emil", "Tobias", "Linus")

# #Keyword Arguments
# def my_function_two(child3, child2, child1):
#   print("The youngest child is " + child3)
# my_function_two(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments : Dùng để gom nhiều tham số có tên (keyword arguments) thành một dictionary(**kwargs)
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
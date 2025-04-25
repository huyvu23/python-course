has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
# Logical operators are used to combine conditional statements
# Logical operators are used to combine conditional statements
# Logical operators are used to combine conditional statements   

if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
# Logical operators are used to combine conditional statements 

if has_high_income and not has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")  

temperature = 35
# >= , <=, >, <, ==, !=
if temperature > 30:
    print("It's a hot day")
elif temperature < 10:  
    print("It's a cold day")
else:
    print("It's neither hot nor cold")
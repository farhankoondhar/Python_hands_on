def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print (f"{key} : {value}")

print_kwargs(name = "Thor", power = "Thunderbolt")
print_kwargs(name = "Ironman", power = "Wealth , Intelligence")

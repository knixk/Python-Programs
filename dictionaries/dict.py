# defining an dict

my_dict = {
    "name": "kanishk",
    "age": 22,
    "country": "IN"
}

name = my_dict["name"]

my_dict["married"] = False

print(name)

for i in my_dict:
    print(type(my_dict[i]))

# or
# print(my_dict)
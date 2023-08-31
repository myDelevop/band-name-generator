def formate_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"


formatted_string = formate_name("roCco", "caLIandRO")
print(formatted_string)

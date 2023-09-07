
is_error = True

a_dictionary = {"item_1": 3}
fruit_list = ["Apple", "Banana", "Pear"]
text_1 = "abc"
text_2 = 5

while is_error is True:
    try:
        # FileNotFoundError
        a_file = open("a_file.txt")

        # KeyError
        print(a_dictionary["not_existing_key"])

        # IndexError
        fruit = fruit_list[3]

        # TypeError
        print(text_1 + text_2)

    except FileNotFoundError as fnt_message:
        # if it doesn't exist we create the file opening in write
        print("Caught FileNotFoundError: " + str(fnt_message))
        a_file = open("a_file.txt", "w")
    except KeyError as ke_message:
        print("Caught KeyError: " + str(ke_message))
        a_dictionary["not_existing_key"] = "Some Value"
    except IndexError as ie_message:
        print("Caught IndexError: " + str(ie_message))
        fruit_list.append("Coconut")
    except TypeError as te_message:
        print("Caught TypeError: " + str(te_message))
        text_1 = 1
        print(text_1 + text_2)
    else:
        print("\n\nYEAH! No anymore errors")
        is_error = False
    finally:
        print("Always Here")

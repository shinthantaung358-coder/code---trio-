is_number = False 

while is_number == False:
    my_number = input("Please give me a number to double")

    if my_number.isdigit():
        my_nuber = float(my_number)
        my_number = my_number * 2
        print(my_number)
        is_number = True

    else:
        print("Please enter a number. You cannot use text in this program")
with open('wuerfel.txt', 'r') as file:
    text = file.read()
    array = text.split()
    integer_array = []

    for element in array:
        try:
            integer_array.append(int(element))
        except ValueError:
            pass

print(integer_array)
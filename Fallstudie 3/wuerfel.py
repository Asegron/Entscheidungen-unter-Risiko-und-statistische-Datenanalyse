with open('wuerfel.txt', 'r') as file:
    text = file.read()
    array = text.split()
    integer_array = [int(x) for x in array]

print(integer_array)
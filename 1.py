def create_pyramid(height):
    k = 1
    output_string = ""
    for y in range(height - 1, -1, -1):
        my_string = " " * y + ("*" + " ") * k
        output_string += my_string + "\n"
        k = k + 1
    return output_string


try:
    h = int(input("Height: "))
    print(create_pyramid(h))
except ValueError:
    print("Please check your height! Use only integer numbers!")

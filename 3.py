from requests import get


def status_code(address):
    return get(address).status_code


try:
    my_address = input("Enter address: ")  # improve url validation with re?
    print(status_code(my_address))
except:
    print("Something wrong, please check your input!")

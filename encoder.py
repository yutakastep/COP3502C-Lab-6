# partner: Anthony Roig

def encode():
    # input for the password
    pass_input = input('Please enter your password to encode: ')
    # turns input string into a list to iterate through
    password = list(pass_input.strip())
    # turns list values into an integer, and then adds 3 to each
    new_pass = [int(x) + 3 for x in password]
    # turns the list back into a string
    encoded_pass = ''.join(str(i) for i in new_pass)
    return encoded_pass


def decode():
    pass


def menu():
    # pretty straightforward, just using a function to simplify the menu code in main
    print('Menu')
    print('-------------')
    print('1. Encode\n2. Decode\n3. Quit')
    print()
    input_option = int(input('Please enter an option: '))
    return input_option


if __name__ == "__main__":
    option = menu()
    while option != 3:
        if option == 1:
            enc_pass = encode()
            print('Your password has been encoded and stored!')
            print()
            option = menu()
        elif option == 2:
            print()
    else:
        pass

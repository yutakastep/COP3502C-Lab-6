# version control encoder/decoder - lab 6
# Author: Yutaka Stephens
# Partner: Guilherme Armin Da Silva Anton

def encode(pass_input):
    # turns input string into a list to iterate through
    password = list(pass_input.strip())
    # turns list values into an integer, and then adds 3 to each
    new_pass = [int(x) + 3 for x in password]
    # turns the list back into a string
    encoded_pass = ''.join(str(i) for i in new_pass)
    return encoded_pass

def decode(original):
    chars = [] # new list/array
    chars[:] = original # splits the string into individual chars in a list/array
    encoded = "" # string that will contain the encoded password
    
    for char in chars: # loop through the items of the list, one char at the time
        num = int(char) # converts the char to int
        num += 3 # adds 3 to it

        # uses f string to convert int to string and concatenates it to whatever was within the string variable
        encoded += f"{num}"

    return encoded

def menu():
    # pretty straightforward, just using a function to simplify the menu code in main
    print('Menu')
    print('-------------')
    print('1. Encode\n2. Decode\n3. Quit')
    print()
    input_option = int(input('Please enter an option: '))
    return input_option

def main():
    # store pass and encoded pass
    src_pass = ""
    enc_pass = ""

    while True:
        option = menu()
        if option == 1:
            src_pass = input('Please enter your password to encode: ')
            enc_pass = encode(src_pass)
            print('Your password has been encoded and stored!')

        elif option == 2:
            if enc_pass == "": # if no source pass was provided
                src_pass = input("Please enter your password to decode: ")
            enc_pass = decode(src_pass)
            print(f"The encoded password is {enc_pass}, and the original password is {src_pass}.")

        elif option == 3: # exit code
            break

        else:
            print("Invalid option")

        print()

# only executes if encoder.py is the main caller file
# does not execute if loaded as a module
if __name__ == "__main__":
    main()

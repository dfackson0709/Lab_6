def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')



def password_encoder(password):
    encoded_password = ''
    for i in range(len(password)):
        if password[i] == '0':
            encoded_password = encoded_password + '3'
        elif password[i] == '1':
            encoded_password = encoded_password + '4'
        elif password[i] == '2':
            encoded_password = encoded_password + '5'
        elif password[i] == '3':
            encoded_password = encoded_password + '6'
        elif password[i] == '4':
            encoded_password = encoded_password + '7'
        elif password[i] == '5':
            encoded_password = encoded_password + '8'
        elif password[i] == '6':
            encoded_password = encoded_password + '9'
        elif password[i] == '7':
            encoded_password = encoded_password + '0'
        elif password[i] == '8':
            encoded_password = encoded_password + '1'
        elif password[i] == '9':
            encoded_password = encoded_password + '2'
    return encoded_password


if __name__ == '__main__':
    print_menu()
    option = int(input('Please enter an option: '))
    while option != 3:
        if option == 1:
            password = str(input('Please enter your password to encode: '))
            new_password = password_encoder(password)
            print('Your password has been encoded and stored!')
            print_menu()
            option = int(input('Please enter an option: '))

        elif option == 2:
            print(f'The encoded password is {new_password} and the original password is {password}')
            print_menu()
            option = int(input('Please enter an option: '))





def main():
    password = get_password()
    print_password(password)


def print_password(password):
    print("PW: ", end='')
    for i in range(len(password)):
        print("*", end='')
    print()


def get_password():
    password = input("PW: ")
    return password


main()

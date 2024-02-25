def main():
    password = get_password()
    print_password(password)


def print_password(password):
    for i in range(len(password)):
        print("*", end='')
    print()


def get_password():
    password = input("PW: ")
    print("PW: ", end='')
    return password


main()

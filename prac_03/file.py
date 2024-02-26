FILE_NAME = "name.txt"

user_name = input("Name: ")
out_file = open(FILE_NAME, "w")
print(user_name, file=out_file)
out_file.close()

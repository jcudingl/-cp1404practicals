FILE_NAME_Q1 = "name.txt"

# Question 1
user_name = input("Name: ")
out_file = open(FILE_NAME_Q1, "w")
print(user_name, file=out_file)
out_file.close()

# Question 2
in_file = open(FILE_NAME_Q1, "r")
name = in_file.read().strip()
print(f"Your name is {name}.")
in_file.close()


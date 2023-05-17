filename = input("Please enter your filename:\n")
name = input("Please enter your name:\n")
address = input("Please enter your address:\n")
phone = input("Please enter your phone number:\n")

with open(filename, 'a') as file_object:
  file_object.write(f"{name}, {address}, {phone}")

with open(filename) as file_object:
  file_output = file_object.read()
  print(file_output)

# The requirements for the program are also listed below.
# Prompt the user for the file name.
# Prompt the user for their name.
# Prompt the user for their street address.
# Prompt the user for their phone number.
# Write the user name, street address, and phone number to a comma-separated line in the file that your user typed in step 1.
# Once the data has been written to the file your program should read the file and display the contents.
#testing comments

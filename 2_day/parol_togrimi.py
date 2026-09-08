# Parol to'g'rimi?

password = input("Enter password: ")

if password.isdigit():
	print("This password consist only of number")
elif password.isalpha():
	if password.isupper():
		print("This password consist only of upper letters")
	elif password.islower():
		print("This password consist only of lower letters")
	else:
		print("This password consist only of letters")
else:
	print("This password consist numbers, letters or other characters")




